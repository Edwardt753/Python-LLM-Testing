import streamlit as st


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="LLM Prompt Security Testing App",
)


st.title("LLM Prompt Security Testing App   ")


# ----------------------------
# Initialize Chat History
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ----------------------------
# Display Previous Messages
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])



# ----------------------------
# User Input
# ----------------------------

prompt = st.chat_input(
    "Type your message here..."
)


if prompt:

    # Save user prompt
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Display user message
    with st.chat_message("user"):
        st.write(prompt)



    # ------------------------------------
    # PLACEHOLDER FOR YOUR LLM CONNECTION
    # ------------------------------------

    response = send_to_llm(prompt)



    # Display LLM response
    with st.chat_message("assistant"):
        st.write(response)


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )



# ----------------------------
# LLM Function
# ----------------------------

def send_to_llm(prompt):

    """
    This function will later send
    your prompt to your hosted LLM.

    Example:

    POST
    http://your-llm-server/api/chat

    Body:
    {
        "prompt": "hello"
    }

    """

    return "LLM response will appear here"