# components/layout.py

import streamlit as st

def configure_page(title: str, icon: str = "💬", layout: str = "centered"):
    """
    Configure Streamlit's global page settings.
    
    Parameters
    ----------
    title : str
        The title displayed on the browser tab.
    icon : str
        Emoji or character to use as the page icon.
    layout : str
        Page layout option ("centered" or "wide").
    """
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout=layout
    )


def render_header(title: str):
    """
    Render the main header of the application.
    
    Parameters
    ----------
    title : str
        The visible title inside the UI.
    """
    st.markdown(
        f"""
        <h1 style="text-align: left; margin-bottom: 10px;">
            {title}
        </h1>
        """,
        unsafe_allow_html=True
    )


def chat_container():
    """
    Creates a persistent Streamlit container to hold chat messages.
    
    Returns
    -------
    Streamlit DeltaGenerator
        A container object where chat messages will be rendered.
    """
    return st.container()
