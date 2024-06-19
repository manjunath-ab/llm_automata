# cat vectorize_docs.py
from langchain_community.document_loaders import WebBaseLoader
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from website_pages_retreiver import getPagesFromSitemap
from pathlib import Path
from dotenv import load_dotenv
import nest_asyncio
import asyncio

nest_asyncio.apply()


dotenv_path = Path('/home/.env')
load_dotenv(dotenv_path=dotenv_path)


urls = list(getPagesFromSitemap("https://docs.snowflake.com/en/"))
print("Number of pages found: ", len(urls))
print("loading pages...")
docs = WebBaseLoader(urls[:2200])
docs.requests_per_second = 5
docs.continue_on_failure=True

docs_list =  docs.aload()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)
print("Number of document splits: ", len(doc_splits))

embeddings= OllamaEmbeddings(model="nomic-embed-text")

# Add to vectorDB
index_name = "snowflake-docs-rag"

vectorstore = PineconeVectorStore.from_documents(doc_splits, embeddings, index_name=index_name)

print("Vectorized all the pages")
