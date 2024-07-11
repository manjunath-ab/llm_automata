import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults

dotenv_path = Path('/home/abhi/.env')
load_dotenv(dotenv_path=dotenv_path)


from typing import List

from typing_extensions import Dict, TypedDict


class GraphState(TypedDict):
    """
    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """

    keys: Dict[str, any]


def fetch_retriever():
    embeddings= OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = PineconeVectorStore(index_name="snowflake-docs-rag", embedding=embeddings)
    return vectorstore.as_retriever(search_kwargs={"k":3})



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


### Retriever Node

def retrieve(state):
    print("---RETRIEVING DOCUMENTS---")
    state_dict = state["keys"]
    question = state_dict["question"]
    retriever=fetch_retriever()
    documents = retriever.invoke(question)
    return {"keys": {"documents": documents, "question": question}}

###Grader Node

def relevance_grader(state):

    print("---CHECK RELEVANCE---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = state_dict["documents"]
    llm = ChatOllama(model="llama3", format="json", temperature=0)
    prompt = PromptTemplate(
        template="""You are a grader assessing relevance of a retrieved document to a user question. \n
        Here is the retrieved document: \n\n {context} \n\n
        Here is the user question: {question} \n
        If the document contains keywords related to the user question, grade it as relevant. \n
        It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
        Provide the binary score as a JSON with a single key 'score' and no premable or explaination.""",
        input_variables=["question","context"],
    )

    chain = prompt | llm | JsonOutputParser()

    # Score
    filtered_docs = []
    search = "No"  # Default do not opt for web search to supplement retrieval
    for d in documents:
        score = chain.invoke(
            {
                "question": question,
                "context": d.page_content,
            }
        )
        grade = score["score"]
        if grade == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            search = "Yes"  # Perform web search
            continue

    return {
        "keys": {
            "documents": filtered_docs,
            "question": question,
            "run_web_search": search,
        }
    }

    return retrieval_grader

##Generator Node
def generate(state):
    prompt = PromptTemplate(
        template="""Imagine you are an expert in snowflake platform and you are to asnwer the user query with this context: \n\n {context} \n\n
        Here is the user question: {question} \n
        """,
        input_variables=["context","question"],
    )

    llm = ChatOllama(model="llama3", temperature=0)
    rag_chain = prompt | llm | StrOutputParser()

    print("---GENERATE---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = state_dict["documents"]


    # Chain
    rag_chain = prompt | llm | StrOutputParser()

    # Run
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {
        "keys": {"documents": documents, "question": question, "generation": generation}
    }



#Rewriter Node
def question_rewrite(state):
    llm = ChatOllama(model="llama3", temperature=0)
    print("---TRANSFORM QUERY---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = state_dict["documents"]


    # Create a prompt template with format instructions and the query
    prompt = PromptTemplate(
        template="""You are generating questions that is well optimized for retrieval in the context of snowflake platform. \n
        Look at the input and try to reason about the underlying sematic intent / meaning. \n
        Here is the initial question:
        \n ------- \n
        {question}
        \n ------- \n
        Answer with just the new formulated question: """ ,
        input_variables=["question"],
    )
     # Prompt
    chain = prompt | llm | StrOutputParser()
    better_question = chain.invoke({"question": question})

    return {
        "keys": {"documents": documents, "question": better_question}
    }


##Web search node:


def web_search(state):

    print("---WEB SEARCH---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = state_dict["documents"]

    tool = TavilySearchResults()
    docs = tool.invoke({"query": question})

    for idx, d in enumerate(docs):
      if not isinstance(d, dict):
        raise TypeError(f"Element at index {idx} is not a dictionary: {docs}")
    filtered_contents = [d["content"] for d in docs if d["content"] is not None]
    web_results = "\n".join(filtered_contents)
    web_results = Document(page_content=web_results)
    documents.append(web_results)

    return {"keys": {"documents": documents, "question": question}}



### Edges


def decide_to_generate(state):
    """
    Determines whether to generate an answer or re-generate a question for web search.

    Args:
        state (dict): The current state of the agent, including all keys.

    Returns:
        str: Next node to call
    """

    print("---DECIDE TO GENERATE---")
    state_dict = state["keys"]
    question = state_dict["question"]
    filtered_documents = state_dict["documents"]
    search = state_dict["run_web_search"]

    if search == "Yes":
        # All documents have been filtered check_relevance
        # We will re-generate a new query
        print("---DECISION: TRANSFORM QUERY and RUN WEB SEARCH---")
        return "question_rewrite"
    else:
        # We have relevant documents, so generate answer
        print("---DECISION: GENERATE---")
        return "generate"
    
import pprint
from langgraph.graph import END, StateGraph

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("retrieve", retrieve)  # retrieve
workflow.add_node("relevance_grader", relevance_grader)  # grade documents
workflow.add_node("generate", generate)  # generatae

workflow.add_node("question_rewrite", question_rewrite)  # transform_query
workflow.add_node("web_search", web_search)  # web search

# Build graph
workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "relevance_grader")
workflow.add_conditional_edges(
    "relevance_grader",
    decide_to_generate,
    {
        "question_rewrite": "question_rewrite",
        "generate": "generate",
    },
)
workflow.add_edge("question_rewrite", "web_search")
workflow.add_edge("web_search", "generate")
workflow.add_edge("generate", END)

# Compile
app = workflow.compile()


import streamlit as st

# Set the title of the app
st.title('Snowflake Sensei')

# Take user input
user_query = st.text_input('Enter you snowflake related query:')

# Respond with a greeting when the user provides their name
if user_query:
    # Run
    inputs = {
    "keys": {
        "question": user_query
    }
    }
    for output in app.stream(inputs):
     for key, value in output.items():
        # Node
        pprint.pprint(f"Node '{key}':")
        # Optional: print full state at each node
        # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
     pprint.pprint("\n---\n")

    # Final generation
    result=value['keys']['generation']
    st.write(f'{result}')
