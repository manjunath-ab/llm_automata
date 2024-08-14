# SnowPlan: A Fully Automated Planning Agent

SnowPlan Demo - Watch Video

[![Loom Video](https://www.loom.com/embed/cd8810c758d24323b642712b68831024?sid=26bdeb28-b616-4162-adbf-1d5ae66c8797)](https://www.loom.com/embed/cd8810c758d24323b642712b68831024?sid=26bdeb28-b616-4162-adbf-1d5ae66c8797)

Click the image above to watch the video.


Welcome to **SnowPlan**, a fully automated planning agent designed to tackle complex tasks by developing and executing a multi-step plan. This agent is built to be both flexible and efficient, adjusting its plan as needed after each step, unlike traditional ReAct-style agents that think one step at a time.

## Overview

The core idea behind SnowPlan is to create a detailed multi-step plan and execute it sequentially. After completing each task, the agent revisits the plan to assess progress and make necessary adjustments. This approach ensures that the agent stays on track and adapts to any new information or challenges that arise during execution.

## Architecture

![image](https://github.com/user-attachments/assets/ea355e83-2d1d-4c95-8f5a-e02b86450c4f)
![image](https://github.com/user-attachments/assets/4240812c-f4ea-4fde-9e24-47e287ff6bdb)





### Advantages of the Plan-and-Execute Style Agent

- **Explicit Long-term Planning:** 
  - Long-term planning can be challenging for even the most advanced LLMs (Large Language Models). SnowPlan addresses this by structuring the planning process explicitly, allowing the agent to keep the end goal in sight while managing intermediate steps effectively.

- **Optimized Model Usage:** 
  - SnowPlan is designed to optimize the use of different models. Smaller or less powerful models can handle execution steps, while larger, more capable models are reserved for the critical task of planning. This leads to more efficient use of computational resources.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)
- **API Keys:**
  - `OPENAI_API_KEY`: Required for interacting with OpenAI's models.
  - `PINECONE_API_KEY`: Required for managing vector databases.
  - `Tavily_api_key`: Required for Tavily services.

- **Dataset Vectorization:**
  - You need to perform vectorization of your dataset before running the agent. This can be done by executing the following script:
  
    ```bash
    python vectorize_docs.py
    ```

<div>
    <a href="https://www.loom.com/share/91d8ccc0ed464bab9902e906e137fd6b">
      <p>taking a look at our pinecone vector DB - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/91d8ccc0ed464bab9902e906e137fd6b">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/91d8ccc0ed464bab9902e906e137fd6b-with-play.gif">
    </a>
  </div>
To enhance the retrieval capabilities and ensure a robust dataset, we will upload Snowflake documents to our Pinecone vector database. This will enable efficient and accurate vector searches.

### Installation and Setup

1. **Clone the Repository:**
   
   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/manjunath-ab/llm_automata.git
   cd snowplan
   ```

2. **Install Dependencies:**

Navigate to the snowPlan folder and install the required dependencies:

```bash
pip install -r requirements.txt

```
This will install all necessary libraries and tools,  the base LLM model (Gpt4o mini) is included using the OPENAI_API_KEY and the orchestration framework (Langraph).

3.**Run the Vectorization Script:**

Before running the main application, ensure that your dataset is properly vectorized by executing:
```bash
python vectorize_docs.py
```
4.**Run the Application:**

Once the dependencies are installed and your dataset is vectorized, you can start the SnowPlan agent through a Streamlit interface by running:
```bash
streamlit run main.py

```
How It Works

Planning Phase:

The agent uses Gpt4o mini to develop a comprehensive plan. This plan outlines the steps required to achieve the desired outcome.
Execution Phase:

The agent follows the plan, executing each step using the appropriate model. After completing each task, the agent revisits the plan to update it based on the new context or any changes in the environment.
Dynamic Adjustment:

Unlike traditional ReAct agents, SnowPlan continuously adapts its strategy, ensuring it remains aligned with the overall objective.
