from pathlib import Path
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings

dotenv_path = Path('/home/.env')
load_dotenv(dotenv_path=dotenv_path)

embeddings= OllamaEmbeddings(model="nomic-embed-text")



vectorstore = PineconeVectorStore(index_name="snowflake-docs-rag", embedding=embeddings)
query = "Explain Snowflake Architecture"
docs = vectorstore.similarity_search(query)
print(docs[0].page_content)