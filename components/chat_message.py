# components/chat_message.py
import streamlit as st


def render_message(role: str, content: str) -> None:
    """
    Render a chat message using Streamlit's chat API.
    
    Parameters
    ----------
    role : str
        Either "user" or "assistant".
    content : str
        The text content of the message.
    """
    if role not in ("user", "assistant"):
        raise ValueError("Role must be either 'user' or 'assistant'.")
    
    with st.chat_message(role):
        st.write(content)

