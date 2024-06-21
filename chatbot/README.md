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

The environment variables are loaded from a `.env` file located at `/home/abhi/.env` using the `load_dotenv` function.Make sure to change the path while running it

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact Abhishek Manjunath at manjunath.ab@northeastern.edu.

