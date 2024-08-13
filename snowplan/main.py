from dotenv import load_dotenv
from pathlib import Path
from typing import Literal
from langgraph.graph import StateGraph, START
import asyncio
from nodes import PlanExecute,Response
from utils import create_agent_executor,create_planner,create_replanner

def load_my_env():

 dotenv_path = Path('/home/abhi/.env')
 load_dotenv(dotenv_path=dotenv_path)



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


async def plan_step(state: PlanExecute):
    planner=create_planner()
    plan = await planner.ainvoke({"messages": [("user", state["input"])]})
    return {"plan": plan.steps}


async def replan_step(state: PlanExecute):
    replanner=create_replanner()
    output = await replanner.ainvoke(state)
    if isinstance(output.action, Response):
        return {"response": output.action.response}
    else:
        return {"plan": output.action.steps}


def should_end(state: PlanExecute) -> Literal["agent", "__end__"]:
    if "response" in state and state["response"]:
        return "__end__"
    else:
        return "agent"


# Define the async function to process events
async def process_events(app, inputs, config):
    try:
        # Asynchronously iterate over events from the app's astream method
        async for event in app.astream(inputs, config=config):
            for k, v in event.items():
                # Process and print the event value if the key is not "__end__"
                if k != "__end__":
                    print(v)
    except Exception as e:
        # Handle any exceptions that may occur during event processing
        print(f"An error occurred: {e}")


async def main():
         load_dotenv()
  
         workflow = StateGraph(PlanExecute)
        # Add the plan node
         workflow.add_node("planner", plan_step)
         # Add the execution step
         workflow.add_node("agent", execute_step)
         # Add a replan node
         workflow.add_node("replan", replan_step)
         workflow.add_edge(START, "planner")
         # From plan we go to agent
         workflow.add_edge("planner", "agent")
         # From agent, we replan
         workflow.add_edge("agent", "replan")
         workflow.add_conditional_edges(
            "replan",
            # Next, we pass in the function that will determine which node is called next.
            should_end,
         )
         app = workflow.compile()
         config = {"recursion_limit": 50}
         inputs = {"input": "how to setup a data engineering pipeline on snowflake?"}
         await process_events(app, inputs, config)


asyncio.run(main())
