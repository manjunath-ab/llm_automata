# LLM Automata

LLM Automata is a collection of projects showcasing various features and capabilities of Large Language Models (LLMs). The repository is organized into several folders, each containing distinct projects with unique functionalities.

## Folders Overview

### CHATBOT
The `CHATBOT` folder contains a simple chatbot built using Mistral as the LLM base. This chatbot leverages Groq for high-speed inference and Streamlit for front-end interaction. It serves as an example of integrating these technologies to create an efficient and responsive conversational agent.

### RAG_WITH_SNOWFLAKE_DOCUMENTATION
The `RAG_WITH_SNOWFLAKE_DOCUMENTATION` folder houses a local LLM chatbot designed to provide solutions based on Snowflake documentation. The goal is to create a conversational AI assistant that can answer questions and offer guidance on Snowflake-related topics.

## Corrective RAG Chat
Within the `RAG_WITH_SNOWFLAKE_DOCUMENTATION` folder, there is a sub-project called Corrective RAG Chat, which follows an advanced architecture. 




Corrective-RAG (CRAG) is a Retrieval-Augmented Generation (RAG) strategy that incorporates self-reflection and self-grading on retrieved documents. The approach is outlined in the following steps:

1. **Document Relevance Check:** If at least one document exceeds the relevance threshold, the process proceeds to the generation phase.
2. **Knowledge Refinement:** Before generation, the documents are partitioned into "knowledge strips," which are then graded, and irrelevant ones are filtered out.
3. **Supplemental Retrieval:** If all documents fall below the relevance threshold or if the grader is unsure, the framework seeks additional data sources. It uses web search, specifically Tavily Search, to supplement retrieval.
4. **Query Re-writing:** Queries are optimized for web search using query re-writing techniques.

The project will implement some of these ideas from scratch using LangGraph. Initially, the knowledge refinement phase will be skipped, but it can be added later as a node if desired. If any documents are deemed irrelevant, supplemental retrieval will be triggered with web search.

### Fully Automated Planning Agent

![image](https://github.com/manjunath-ab/llm_automata/assets/114261603/4d17e41a-8f8d-4595-869a-b8ab8633d4dc)

The repository also includes a fully automated planning agent. The core idea behind this agent is to develop a multi-step plan and execute it one step at a time. After completing a particular task, the agent revisits the plan and modifies it as appropriate. This approach contrasts with a typical ReAct style agent that thinks one step at a time.

#### Advantages of the Plan-and-Execute Style Agent:
- **Explicit Long-term Planning:** Even strong LLMs can struggle with long-term planning, but this approach facilitates it effectively.
- **Optimized Model Usage:** The agent can use smaller/weaker models for the execution steps, reserving larger/better models for the planning steps.

## Getting Started
To get started with any of the projects in this repository, follow the instructions provided in the respective folders. Each folder contains a detailed README with setup instructions, dependencies, and usage guidelines.


