from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from nodes import Plan,Act
from langchain import hub
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

def fetch_retriever():
    embeddings= OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = PineconeVectorStore(index_name="snowflake-docs-rag", embedding=embeddings)
    return vectorstore.as_retriever(search_kwargs={"k":3})

def create_my_retriever():
    retriever= create_retriever_tool(
    fetch_retriever(),
    "knowledge_base_for_snowflake",
    "This is a retreiver tool for which has information on snowflake documentation",
    )
    return retriever


def create_planner():

 planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.""",
        ),
        ("placeholder", "{messages}"),
    ]
)
 planner = planner_prompt | ChatOpenAI(
    model="gpt-3.5-turbo", temperature=0
).with_structured_output(Plan)

 return planner

def create_agent_executor():
    tools = [TavilySearchResults(max_results=3),create_my_retriever()]
    prompt = hub.pull("wfh/react-agent-executor")
    prompt.pretty_print()

# Choose the LLM that will drive the agent
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    agent_executor = create_react_agent(llm, tools, messages_modifier=prompt)
    return agent_executor



def create_replanner():
 replanner_prompt = ChatPromptTemplate.from_template(
         """For the given objective, come up with a simple step by step plan. \
     This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
     The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

     Your objective was this:
     {input}

     Your original plan was this:
     {plan}

     You have currently done the follow steps:
     {past_steps}

     Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan."""
     )


 replanner = replanner_prompt | ChatOpenAI(
    model="gpt-3.5-turbo", temperature=0
   ).with_structured_output(Act)
 return replanner