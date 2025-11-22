# session_manager.py

import uuid
import streamlit as st

class SessionManager:
    """
    Manages Streamlit session state including:
    - Persistent session UUID
    - Chat message history
    - Reset functionality
    - Utility helpers for storing/retrieving state
    """

    SESSION_ID_KEY = "session_id"
    MESSAGE_HISTORY_KEY = "messages"

    @staticmethod
    def initialize_session():
        """
        Initialize session state variables if not already present.
        """
        if SessionManager.SESSION_ID_KEY not in st.session_state:
            st.session_state[SessionManager.SESSION_ID_KEY] = uuid.uuid4().hex

        if SessionManager.MESSAGE_HISTORY_KEY not in st.session_state:
            st.session_state[SessionManager.MESSAGE_HISTORY_KEY] = []

    @staticmethod
    def get_session_id() -> str:
        """
        Return the persistent session UUID.
        """
        return st.session_state.get(SessionManager.SESSION_ID_KEY)

    @staticmethod
    def add_message(role: str, content: str):
        """
        Append a message to the chat history stored in session_state.
        
        Parameters
        ----------
        role : str
            "user" or "assistant"
        content : str
            Message text.
        """
        if role not in ("user", "assistant"):
            raise ValueError("Role must be 'user' or 'assistant'.")

        st.session_state[SessionManager.MESSAGE_HISTORY_KEY].append(
            {"role": role, "content": content}
        )

    @staticmethod
    def get_messages():
        """
        Retrieve full message history.
        """
        return st.session_state.get(SessionManager.MESSAGE_HISTORY_KEY, [])

    @staticmethod
    def clear_history():
        """
        Reset conversation and regenerate a new session ID.
        """
        st.session_state[SessionManager.SESSION_ID_KEY] = uuid.uuid4().hex
        st.session_state[SessionManager.MESSAGE_HISTORY_KEY] = []
