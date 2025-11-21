# ui/components.py
import streamlit as st
from typing import List, Dict


def render_chat_history(messages: List[Dict[str, str]]) -> None:
    """
    Render all messages stored in the session state using st.chat_message.
    
    Parameters:
        messages (list): A list of dicts with keys: role, content.
    """
    for msg in messages:
        role = msg.get("role", "assistant")
        content = msg.get("content", "")

        if role not in ("user", "assistant"):
            role = "assistant"

        with st.chat_message(role):
            st.markdown(content)


def render_system_message(text: str) -> None:
    """
    Display a system-style assistant message (informational).
    """
    with st.chat_message("assistant"):
        st.info(text)
