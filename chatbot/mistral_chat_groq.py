# cat de_prod.py
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq

dotenv_path = Path('/home/abhi/.env')
load_dotenv(dotenv_path=dotenv_path)
model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

# Function to create system template
def create_system_template():
    SYSTEM_TEMPLATE = """
    Imagine you are a Data Engineering expert. Introduce yourself as Marco.
    Ask the user to present a data engineering problem, then ask as many questions needed 
    about the problem to get clarity around the subject and then present a step by step 
    solution based on the problem.
    """
    return SYSTEM_TEMPLATE

# Function to retrieve session history based on session_id
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if 'store' not in st.session_state:
        st.session_state.store = {}
        
    if session_id not in st.session_state.store:
        print("Session doesn't exist")
        st.session_state.store[session_id] = ChatMessageHistory()
    
    return st.session_state.store[session_id]

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", create_system_template()),
    MessagesPlaceholder(variable_name="messages"),
])

# Chain the prompt, model, and output parser
chain = prompt | model

# Create a RunnableWithMessageHistory instance
with_message_history = RunnableWithMessageHistory(chain, get_session_history)

# Define Streamlit app
def main():
    st.title("Data Engineering Expert Chatbot")

    # Define config for the session
    config = {"configurable": {"session_id": "de123"}}

    # Input box for user message
    user_input = st.text_input("You:", "")
    response_container = st.empty()
    # Button to send the message and get the response
    if st.button("Send Message"):
        response_text = ""
        for response in with_message_history.stream(
            [HumanMessage(content=user_input)],
            config=config,
        ):
            response_text += response.content
            response_container.write(f"Marco the DE Expert:\n\n{response_text}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
