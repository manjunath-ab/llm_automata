# cat vectorize_docs.py
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




embeddings= OllamaEmbeddings(model="nomic-embed-text")

batch_size = 10
num_docs = len(docs_list)
print(f"Total number of batches is: {num_docs//batch_size}")
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=50
  )


for i in range(0, num_docs, batch_size):
  # Split documents into batches
  batch_docs = docs_list[i:i+batch_size]

  # Create document splits
  doc_splits = text_splitter.split_documents(batch_docs)


  # Add batch to vector store (simulated)
  vectorstore = PineconeVectorStore.from_documents(doc_splits, embeddings, index_name="snowflake-docs-rag")

  # Print progress after each batch
  print(f"Processed documents {i+1} to {min(i+batch_size, num_docs)}")

print("Vectorized all documents (in batches)")