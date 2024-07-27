# RAG Chatbot Evaluation using DeepEval

This project aims to evaluate a Retrieval-Augmented Generation (RAG) chatbot using DeepEval, focusing specifically on the Answer Relevancy metric. The Answer Relevancy metric measures the quality of your RAG pipeline's generator by evaluating how relevant the actual output of your LLM application is compared to the provided input.
I have generated a excel document by testing the rag chatbot.
## Metrics

### Answer Relevancy

The Answer Relevancy metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score. The score is calculated according to the following equation:

\[ \text{Answer Relevancy} = \frac{\text{Number of Relevant Statements}}{\text{Total Number of Statements}} \]

Where:
- **Number of Relevant Statements**: The count of statements in the chatbot's response that are considered relevant to the input question.
- **Total Number of Statements**: The total count of statements in the chatbot's response.

### Faithfulness

The faithfulness metric measures the quality of your RAG pipeline's generator by evaluating whether the actual output factually aligns with the contents of your retrieval context. DeepEval's faithfulness metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score. The FaithfulnessMetric score is calculated according to the following equation:

\[ \text{Faithfulness} = \frac{\text{Number of Truthful Claims}}{\text{Total Number of Claims}} \]

Where:
- **Number of Truthful Claims**: The count of claims in the chatbot's response that are factually correct.
- **Total Number of Claims**: The total count of claims in the chatbot's response.

### Contextual Precision

The contextual precision metric measures your RAG pipeline's retriever by evaluating whether nodes in your retrieval context that are relevant to the given input are ranked higher than irrelevant ones. DeepEval's contextual precision metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.
![image](https://github.com/user-attachments/assets/9dc382bb-b925-4632-a5e5-e3b3c97f6bee)

### Contextual Recall

The contextual recall metric measures the quality of your RAG pipeline's retriever by evaluating the extent to which the retrieval context aligns with the expected output. DeepEval's contextual recall metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.
![image](https://github.com/user-attachments/assets/c4751259-c10a-4f75-884a-104de388b323)

### Contextual Relevancy

The contextual relevancy metric measures the quality of your RAG pipeline's retriever by evaluating the overall relevance of the information presented in your retrieval context for a given input. DeepEval's contextual relevancy metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.
![image](https://github.com/user-attachments/assets/ec267a00-1a5c-40c5-a452-31194f8176d0)

## Getting Started

These instructions will guide you through the setup and evaluation process.

### Prerequisites

- Python 3.x
- Pandas
- DeepEval library

You can install the required libraries using pip.

```sh
pip install deepeval
```


### Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure your chatbot's output data and the corresponding input data are available in a suitable format (e.g., CSV, JSON).

### Running the Evaluation

1. Load your chatbot's output data into a pandas DataFrame.
2. Use DeepEval to calculate the relevant metric scores for each response.
3. Analyze the results to understand the performance of your RAG chatbot.

## Methods to Improve Metrics

### Improving Answer Relevancy

1. **Enhance the Retrieval Mechanism**: Improve the quality of retrieved documents or passages by fine-tuning the retrieval algorithm. This could involve optimizing the ranking model to prioritize more relevant information.

2. **Contextual Embeddings**: Utilize advanced contextual embeddings like BERT or GPT to better understand the context of the input question and generate more relevant responses.

3. **Response Filtering**: Implement a filtering mechanism to remove irrelevant or low-quality responses before presenting the final answer to the user.

### Improving Faithfulness

1. **Fact-Checking Module**: Integrate a fact-checking module that verifies the factual accuracy of the generated responses against the retrieved context before finalizing the answer.

2. **Knowledge Base Integration**: Enhance the RAG pipeline by integrating it with a reliable and up-to-date knowledge base to cross-verify the facts mentioned in the response.

3. **Training with Factually Correct Data**: Fine-tune the generator model on datasets that emphasize factual correctness to improve its ability to generate truthful statements.

### Documentation and Analysis

- **Document Changes**: Keep a detailed record of all modifications made to the RAG pipeline, including changes to algorithms, models, and integration of new modules.
- **Performance Analysis**: After implementing the proposed methods, analyze their impact on the overall performance of the RAG pipeline. This includes measuring improvements in the Answer Relevancy and Faithfulness metrics and comparing them with baseline performance.
- **Iterative Refinement**: Based on the analysis, continuously refine and optimize the methods to achieve better performance.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the DeepEval team for providing the tools and metrics used in this evaluation.
