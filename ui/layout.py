# ui/layout.py
import streamlit as st
from config.settings import (
    APP_TITLE,
    APP_ICON,
    APP_LAYOUT,
    APP_INITIAL_SIDEBAR_STATE,
)


def configure_page() -> None:
    """
    Configure global Streamlit page settings such as:
    - Page title
    - Icon
    - Layout
    - Sidebar visibility
    """
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout=APP_LAYOUT,
        initial_sidebar_state=APP_INITIAL_SIDEBAR_STATE,
        menu_items={
            "Get Help": None,
            "Report a Bug": None,
            "About": "Frontend chat UI powered by Streamlit and n8n backend.",
        },
    )


def render_sidebar() -> None:
    """
    Render the sidebar UI components:
    - App description
    - Session ID display
    """
    with st.sidebar:
        st.header("⚙️ Session Info")
        st.markdown(
            """
            This is a Streamlit-based frontend connected to an n8n workflow.
            All conversation logic, memory and embeddings are handled by n8n.
            """
        )

        if "session_id" in st.session_state:
            st.code(f"Session ID: {st.session_state['session_id']}", language="bash")

        st.divider()
        st.caption("Built with Streamlit.")
