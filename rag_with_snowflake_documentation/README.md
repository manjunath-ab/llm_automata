![image](https://github.com/manjunath-ab/snowflake_sensei/assets/114261603/9a0c0f5f-cdcd-49d0-bd25-5e0f8d5b6dfc)

### Uploading Snowflake Docs to Pinecone Vector Database

<div>
    <a href="https://www.loom.com/share/91d8ccc0ed464bab9902e906e137fd6b">
      <p>taking a look at our pinecone vector DB - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/91d8ccc0ed464bab9902e906e137fd6b">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/91d8ccc0ed464bab9902e906e137fd6b-with-play.gif">
    </a>
  </div>
To enhance the retrieval capabilities and ensure a robust dataset, we will upload Snowflake documents to our Pinecone vector database. This will enable efficient and accurate vector searches.

#### Steps to Upload Documents

1. **Install Necessary Libraries**:
   - Ensure you have the necessary libraries installed

2. **Set Up Pinecone**:
   - Sign up for a Pinecone account if you don't have one.
   - Create an index in your Pinecone dashboard.

3. **Vectorize and Upload Documents**:
   - Replace the placeholder Pinecone API key in your script with your actual Pinecone API key.
   - Run the script provided to vectorize your documents and upload them to Pinecone.

NOTE: Make sure to replace the pinecone and tavily api keys.

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

[[RAG with snowflake docs]](https://www.loom.com/share/ae82c5dc67d847c0870c3c52e06842d0?sid=6389af0e-f80c-4963-b020-7c3487754172)
<div>
    <a href="https://www.loom.com/share/ae82c5dc67d847c0870c3c52e06842d0">
      <p>RAG with Snowflake Documentation - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/ae82c5dc67d847c0870c3c52e06842d0">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/ae82c5dc67d847c0870c3c52e06842d0-with-play.gif">
    </a>
  </div>
### Notes

- Ensure you have a GPU available for the runtime to avoid slow processing times.
- This implementation focuses on the basic framework and can be extended with additional features like knowledge refinement in future iterations.

Feel free to reach out for any questions or further assistance.

---
