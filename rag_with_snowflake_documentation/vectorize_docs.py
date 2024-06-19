from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from website_pages_retreiver import getPagesFromSitemap

urls = list(getPagesFromSitemap("https://docs.snowflake.com/en/"))
print("Number of pages found: ", len(urls))
print("loading pages...")
docs = [WebBaseLoader(url).load() for url in urls[:10]]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)
print("Number of document splits: ", len(doc_splits))

# Add to vectorDB
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=OllamaEmbeddings(),
)
retriever = vectorstore.as_retriever()
print(retriever)