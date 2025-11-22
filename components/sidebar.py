# components/sidebar.py

import streamlit as st

def render_sidebar(reset_callback=None):
    """
    Render the application sidebar with additional controls and information.
    
    Parameters
    ----------
    reset_callback : callable, optional
        Function to call when the user clicks the 'Reset chat' button.
    """
    with st.sidebar:
        st.header("⚙️ Settings")

        st.markdown("### Chat Controls")

        if reset_callback is not None:
            if st.button("🗑️ Reset conversation"):
                reset_callback()

        st.markdown("---")
        st.markdown("### Model Info")
        st.markdown("- **Backend:** n8n Webhook")
        st.markdown("- **Frontend:** Streamlit UI")
        st.markdown("- **Memory:** Postgres Chat Memory (Supabase)")
        
        st.markdown("---")
        st.caption("💡 This is a modular sidebar. You can extend it later.")
