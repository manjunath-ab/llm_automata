## Prerequisites

Before getting started, make sure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Getting Started

Follow these steps to set up and run the Snowflake Sensei chatbot:

1. **Pull the OllaMa Docker Image**

```bash
docker pull ollama/ollama
```
2. **Start the OllaMa Container**

3. **Update Package Manager and Install Required Packages**

```bash
apt-get update
apt-get install -y pip git
```

4.**Install Python Requirements**
```bash
pip install -r requirements.txt
```

5. **Pull LLaMa3 and Nomic-Embed-Text Models**
```bash
ollama pull llama3
ollama pull nomic-embed-text
```
6. **Create a Pinecone Account and Obtain an API Key**
Sign up for a Pinecone account and create a new project. Obtain the API key for your project.
8. **Store Pinecone API Key in Environment Variable**
Create a .env file in the project root and store your Pinecone API key as an environment variable:
```BASH
PINECONE_API_KEY=your_pinecone_api_key_here
```

## Execution

1. Run
```bash
python3 vectorize.py
```
