# LLM Automata


LLM Automata has many features categorized by the folders.It is a local large language model (LLM) chatbot that specializes in providing solutions based on Snowflake documentation. The goal is to create a conversational AI assistant that can answer questions and offer guidance on Snowflake-related topics .


I have built Corrective RAG Chat within the RAG with snowflake folder that follows this architecture:
![image](https://github.com/manjunath-ab/snowflake_sensei/assets/114261603/48124772-8300-41f3-a71d-d65eca768ee4)

Corrective-RAG (CRAG) is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents.

In the paper here, a few steps are taken:

If at least one document exceeds the threshold for relevance, then it proceeds to generation
Before generation, it performns knowledge refinement
This partitions the document into "knowledge strips"
It grades each strip, and filters our irrelevant ones
If all documents fall below the relevance threshold or if the grader is unsure, then the framework seeks an additional datasource
It will use web search to supplement retrieval
We will implement some of these ideas from scratch using LangGraph:

Let's skip the knowledge refinement phase as a first pass. This can be added back as a node, if desired.
If any documents are irrelevant, let's opt to supplement retrieval with web search.
We'll use Tavily Search for web search.
Let's use query re-writing to optimize the query for web search.


In the other flow : [Undecided]

