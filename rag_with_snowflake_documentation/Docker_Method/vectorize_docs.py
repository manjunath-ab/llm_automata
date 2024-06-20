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

embeddings= OllamaEmbeddings(model="nomic-embed-text")
total_docs=2200






batch_size = 10

print(f"Total number of batches is: {total_docs/batch_size}")
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=50
  )


for i in range(0, total_docs, batch_size):
  # Split documents into batches

  docs = WebBaseLoader(urls[i:i+batch_size])
  docs.requests_per_second = 5
  docs.continue_on_failure=True

  docs_list =  docs.aload()
  batch_docs = docs_list

  # Create document splits
  doc_splits = text_splitter.split_documents(batch_docs)


  # Add batch to vector store (simulated)
  vectorstore = PineconeVectorStore.from_documents(doc_splits, embeddings, index_name="snowflake-docs-rag")

  # Print progress after each batch
  print(f"Processed documents {i+1} to {min(i+batch_size, total_docs)}")

print("Vectorized all documents (in batches)")