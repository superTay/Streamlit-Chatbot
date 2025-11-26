# ui/components.py
from typing import List, Dict
import streamlit as st

from components.chat_message import render_message


def render_chat_history(messages: List[Dict[str, str]]) -> None:
    """
    Render all messages stored in the session state using the chat_message component.
    
    Parameters
    ----------
    messages : list of dict
        Each dict must contain:
            - role: "user" or "assistant"
            - content: text of the message
    """
    for msg in messages:
        role = msg.get("role", "assistant")
        content = msg.get("content", "")

        if role not in ("user", "assistant"):
            role = "assistant"

        render_message(role, content)


def render_system_message(text: str) -> None:
    """
    Display a system-style assistant message (informational / error).
    """
    with st.chat_message("assistant"):
        st.info(text)

