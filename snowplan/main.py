import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from typing import Literal
from langgraph.graph import StateGraph, START
import asyncio
from nodes import PlanExecute, Response
from utils import create_agent_executor, create_planner, create_replanner
import io
import json

# Function to load environment variables
def load_my_env():
    dotenv_path = Path('/home/abhi/.env')
    load_dotenv(dotenv_path=dotenv_path)

# Async function to execute a step in the plan
async def execute_step(state: PlanExecute):
    plan = state["plan"]
    plan_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(plan))
    task = plan[0]
    task_formatted = f"""For the following plan:
    {plan_str}\n\nYou are tasked with executing step {1}, {task}."""
    agent_response = await create_agent_executor().ainvoke(
        {"messages": [("user", task_formatted)]}
    )
    return {
        "past_steps": (task, agent_response["messages"][-1].content),
    }

# Async function to create a plan
async def plan_step(state: PlanExecute):
    planner = create_planner()
    plan = await planner.ainvoke({"messages": [("user", state["input"])]})
    return {"plan": plan.steps}

# Async function to replan a step
async def replan_step(state: PlanExecute):
    replanner = create_replanner()
    output = await replanner.ainvoke(state)
    if isinstance(output.action, Response):
        return {"response": output.action.response}
    else:
        return {"plan": output.action.steps}

# Function to determine if the process should end
def should_end(state: PlanExecute) -> Literal["agent", "__end__"]:
    if "response" in state and state["response"]:
        return "__end__"
    else:
        return "agent"

# Async function to process events and display them in Streamlit
async def process_events(app, inputs, config,log_file):
    event_container = st.empty()  # Streamlit container to display events
    try:
        async for event in app.astream(inputs, config=config):
            for k, v in event.items():
                if k != "__end__":
                    event_container.write(v)
                    log_file.write(json.dumps({k: v}, indent=2) + "\n")
                    log_file.flush()
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Main function to run the app
async def main():
    st.image("/home/abhi/llm_automata/snowplan/snowplannerimage.jpeg")
    st.title("Snow Plan")
    st.sidebar.write(
    "Introducing **SnowPlan**—your ultimate solution for effortless problem-solving with the Snowflake platform! "
    "Simply input your challenge, and let SnowPlan take over. With its cutting-edge technology, SnowPlan harnesses a vast knowledge base "
    "and the latest internet resources to thoroughly analyze your issue. It crafts a detailed plan, executes each step, and continuously adapts "
    "based on real-time data and feedback. The result? Tailor-made, optimized solutions that meet your exact needs. Elevate your problem-solving game "
    "with SnowPlan—where innovation meets efficiency!"
)

    load_my_env()
    
    workflow = StateGraph(PlanExecute)
    workflow.add_node("planner", plan_step)
    workflow.add_node("agent", execute_step)
    workflow.add_node("replan", replan_step)
    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "agent")
    workflow.add_edge("agent", "replan")
    workflow.add_conditional_edges("replan", should_end)

    app = workflow.compile()
    config = {"recursion_limit": 50}
    user_input = st.text_input("Enter your query", "how to setup a data engineering pipeline on snowflake?")
    inputs = {"input": user_input}
    
    if st.button("Run Workflow"):
        log_file = io.StringIO()  # In-memory file to store log
        await process_events(app, inputs, config,log_file)
        log_file.seek(0)  # Reset file pointer to the beginning
        
        # Convert log to downloadable file
        st.download_button(
            label="Download Plan",
            data=log_file.getvalue(),
            file_name="workflow.txt",
            mime="text/plain",
        )

if __name__ == "__main__":
    asyncio.run(main())
