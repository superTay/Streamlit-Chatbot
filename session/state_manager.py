# session/state_manager.py
import uuid
import streamlit as st


def init_session_state() -> None:
    """
    Initialize the essential Streamlit session state variables:
    
    - messages: list storing chat history
    - session_id: unique ID used to link a conversation
    - is_waiting_response: flag to prevent multiple requests in parallel
    """
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())

    if "is_waiting_response" not in st.session_state:
        st.session_state["is_waiting_response"] = False


def add_message(role: str, content: str) -> None:
    """
    Add a message to the chat history.
    
    Parameters:
        role (str): "user" or "assistant"
        content (str): message text
    """
    st.session_state["messages"].append({
        "role": role,
        "content": content,
    })


def get_history():
    """Return the full stored chat history."""
    return st.session_state.get("messages", [])


def clear_history() -> None:
    """Erase the conversation history."""
    st.session_state["messages"] = []
