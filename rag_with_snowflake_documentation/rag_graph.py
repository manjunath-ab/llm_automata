from pathlib import Path
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser

def load_env():
    dotenv_path = Path('/home/.env')
    load_dotenv(dotenv_path=dotenv_path)

def fetch_vectorstore():
    embeddings= OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = PineconeVectorStore(index_name="snowflake-docs-rag", embedding=embeddings)
    return vectorstore

### Retrieval Grader

def retrieval_grader():
    llm = ChatOllama(model="llama3", format="json", temperature=0)
    prompt = PromptTemplate(
    template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
    Here is the retrieved document: \n\n {document} \n\n
    Here is the user question: {question} \n
    If the document contains keywords related to the user question, grade it as relevant. \n
    It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question. \n
    Provide the binary score as a JSON with a single key 'score' and no premable or explanation.""",
    input_variables=["question", "document"],
)
    retrieval_grader = prompt | llm | JsonOutputParser()

    return retrieval_grader




def main():
    load_env()
    vectorstore=fetch_vectorstore()
    retriever = vectorstore.as_retriever()
    #retrieval grader:
    grader = retrieval_grader()
    question = "Explain Snowflake Architecture"
    docs = retriever.invoke(question)
    print("Retrieved documents: ", len(docs))
    doc_txt = docs[1].page_content
    for item in grader.stream({"question": question, "document": doc_txt}):
        print(item)

if __name__ == "__main__":
    main()

    






