![image](https://github.com/manjunath-ab/snowflake_sensei/assets/114261603/9a0c0f5f-cdcd-49d0-bd25-5e0f8d5b6dfc)
## Corrective-RAG (CRAG) Strategy

CRAG is an advanced strategy for Retrieval-Augmented Generation (RAG) that enhances the retrieval process by incorporating self-reflection and self-grading on the retrieved documents. The goal is to ensure high relevance and accuracy of the documents used for generation. The process follows these steps:

1. **Initial Document Retrieval**:
   - Retrieve only 3 documents initially.

2. **Relevance Grading**:
   - Each document is graded for relevance.
   - If any document is deemed irrelevant, the system supplements the retrieval with a web search using Tavily Search.
   - Query re-writing is used to optimize the web search query.

3. **Final Document Selection**:
   - The final set of documents is used for generation.

### Implementation Steps

We will implement this using LangGraph, following these steps:

1. **Clone the Repository**:
   - Clone the repository to your local machine.

2. **Run the Notebook**:
   - Open the notebook and connect it to a GPU runtime. This is essential for efficient processing, as running locally without an NVIDIA GPU can be very slow.
   - We have used a Colab notebook for this purpose.

3. **Skipping Knowledge Refinement**:
   - For the initial implementation, we will skip the knowledge refinement phase. This phase can be added back later as a node if desired.

4. **Supplement with Web Search**:
   - If any of the retrieved documents are found irrelevant, use Tavily Search to find additional relevant documents.
   - Use query re-writing to refine and optimize the search queries.

5. **Document Generation**:
   - After ensuring all documents are relevant, proceed to generate the final result.

### Demo

A demo of the project can be seen below.

[Include a link or embed the demo video here]

### Notes

- Ensure you have a GPU available for the runtime to avoid slow processing times.
- This implementation focuses on the basic framework and can be extended with additional features like knowledge refinement in future iterations.

Feel free to reach out for any questions or further assistance.

---
