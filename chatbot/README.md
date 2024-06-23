<div>
    <a href="https://www.loom.com/share/c51e7374330b48b4b785c2a3aaaa424e">
      <p>Data Engineering Chatbot using Mistral  - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/c51e7374330b48b4b785c2a3aaaa424e">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/c51e7374330b48b4b785c2a3aaaa424e-with-play.gif">
    </a>
  </div>
  
```markdown
# Data Engineering Expert Chatbot

This project is a Streamlit application that simulates a chat with a Data Engineering expert named Marco. Marco can assist with data engineering problems by asking clarifying questions and providing step-by-step solutions.

## Installation

To run this project, you'll need to install the required dependencies listed in the `requirements.txt` file. You can do this by running the following command:

```sh
pip install -r requirements.txt
```

## Usage
Before you run the main file, make sure to create your own groq api key and load in the .env file and change the path.
To start the Streamlit app, navigate to the directory containing the `mistral_chat_groq.py` file and run the following command:

```sh
streamlit run mistral_chat_groq.py
```

## Project Structure

- `mistral_chat_groq.py`: The main Python script that runs the Streamlit app.
- `requirements.txt`: A file listing all the dependencies required to run the project.

## Code Overview

### Imports

The script imports several libraries and modules required for the application
### Loading Environment Variables

Make a Groq API Key and store it in the environment variables loaded from a `.env` file located at `/home/abhi/.env` using the `load_dotenv` function.Make sure to change the path while running it

### Model Initialization

The `ChatGroq` model is initialized with specific parameters, such as `temperature` and `model_name`.

### System Template Creation

A function `create_system_template` is defined to create a system message template, which guides the behavior of the chatbot.

### Session History Management

A function `get_session_history` is defined to retrieve or initialize a chat history based on a `session_id`. This ensures that the chat history is maintained across user interactions.

### Chat Prompt Template

A chat prompt template is created using the `ChatPromptTemplate` class, which includes the system template and a placeholder for messages.

### Runnable with Message History

The `RunnableWithMessageHistory` class is used to chain the prompt, model, and output parser, along with the session history.

### Streamlit Application

The `main` function defines the Streamlit app:
- It sets the title of the app.
- Configures the session with a `session_id`.
- Provides an input box for the user to enter messages.
- Includes a button to send the message and display the response from Marco.

### Running the Application

The script runs the `main` function if executed as the main module.

## Example

After starting the Streamlit app, you can interact with Marco by typing your data engineering problem into the input box and clicking the "Send Message" button. Marco will respond by asking clarifying questions and providing a step-by-step solution.

## Usefulness of Responses

The Data Engineering Expert Chatbot, Marco, is designed to provide highly useful and context-specific responses to data engineering problems. The key aspects that make the responses valuable for the user base include:

### Expert Guidance
Marco simulates a conversation with a seasoned data engineering expert, offering solutions that are practical and aligned with industry best practices.

### Interactive Problem-Solving
The chatbot engages users in a dialogue, asking clarifying questions to fully understand the problem before suggesting solutions. This ensures that responses are tailored to the user's specific context and needs.

### Step-by-Step Solutions
Marco provides detailed, step-by-step instructions to address the problem, making it easier for users to follow and implement the solutions effectively.

### Real-Time Feedback
Users receive immediate feedback and solutions to their queries, which is crucial for time-sensitive data engineering tasks.

### Continuous Improvement
The chatbot leverages session histories to maintain context across interactions, allowing for more coherent and informed responses over time.

These features ensure that users receive high-quality, actionable advice that can significantly aid in resolving complex data engineering issues efficiently.

## Variety of Queries Handled

The Data Engineering Expert Chatbot is capable of addressing a wide range of queries related to data engineering. Here are some examples of the types of queries the application handles:

### Data Pipeline Design
- How to design and implement a scalable ETL pipeline?
- Best practices for data ingestion from multiple sources.

### Database Management
- How to optimize database performance?
- Strategies for data partitioning and indexing.

### Data Warehousing
- How to design a data warehouse for a large e-commerce platform?
- Tips for integrating real-time data streams into a data warehouse.

### Big Data Technologies
- Differences between Hadoop and Spark and when to use each.
- How to implement data processing using Apache Kafka?

### Data Quality and Governance
- Techniques for ensuring data quality in data lakes.
- Best practices for data governance and compliance.

### Data Modeling
- How to create an efficient data model for an IoT application?
- Normalization vs. denormalization in database design.

### Cloud Data Engineering
- How to migrate on-premises data infrastructure to AWS?
- Using Google BigQuery for large-scale data analytics.

### Data Security
- Methods for securing sensitive data in transit and at rest.
- Implementing role-based access control in a data platform.

By addressing such a diverse array of topics, the chatbot caters to a broad audience, from novice data engineers to experienced professionals seeking advanced solutions. This versatility makes it an invaluable tool for anyone involved in data engineering.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact Abhishek Manjunath at manjunath.ab@northeastern.edu.

