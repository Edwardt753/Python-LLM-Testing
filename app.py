import streamlit as st

from llm.client import send_to_llm
from utils.session import initialize_chat, add_message


# ----------------------------
# Page Setup
# ----------------------------

st.set_page_config(
    page_title="My LLM Chatbot",
    page_icon="🤖"
)


st.title("🤖 My Hosted LLM Chatbot")


# ----------------------------
# Initialize session
# ----------------------------

initialize_chat()



# ----------------------------
# Display chat history
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])



# ----------------------------
# User Input
# ----------------------------

prompt = st.chat_input(
    "Type your message..."
)


if prompt:

    # Save user message
    add_message(
        "user",
        prompt
    )


    # Display user message
    with st.chat_message("user"):
        st.write(prompt)



    # Send to LLM
    response = send_to_llm(
        prompt
    )


    # Display response
    with st.chat_message("assistant"):
        st.write(response)



    # Save response
    add_message(
        "assistant",
        response
    )