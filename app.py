# app.py
import streamlit as st

from config.settings import APP_TITLE, APP_ICON
from session.state_manager import init_session_state, add_message, get_history, clear_history
from ui.layout import configure_page, render_sidebar, inject_theme_css
from ui.components import render_chat_history, render_system_message
from services.n8n_client import send_message_to_n8n
from services.stream_utils import stream_text


# --- Page setup ---
configure_page()
inject_theme_css()  # <-- NEW: apply global theme CSS

# --- Session state initialization ---
init_session_state()

# --- Sidebar ---
render_sidebar()

# --- Header ---
st.title(f"{APP_ICON} {APP_TITLE}")

# Optional: Clear chat button
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🧹 Clear Chat"):
        clear_history()
        st.rerun()

st.divider()

# --- Render history ---
history = get_history()
render_chat_history(history)

# --- User input ---
prompt = st.chat_input("Write your message...")

if prompt:
    # Save user message
    add_message("user", prompt)

    # Render immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prevent spamming multiple requests
    st.session_state["is_waiting_response"] = True

    # --- Send to n8n ---
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_text = send_message_to_n8n(
                    prompt=prompt,
                    session_id=st.session_state["session_id"],
                )

                full_response = st.write_stream(stream_text(response_text))

        add_message("assistant", full_response)

    except Exception as e:
        render_system_message(
            f"❌ Error while communicating with n8n backend:\n\n`{e}`"
        )

    finally:
        st.session_state["is_waiting_response"] = False

