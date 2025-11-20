
# config/settings.py
import os

# ---------- APP CONFIG ----------
APP_TITLE = "Assistant n8n / GPT"
APP_ICON = "💬"
APP_LAYOUT = "centered"
APP_INITIAL_SIDEBAR_STATE = "collapsed"

# ---------- N8N WEBHOOK CONFIG ----------
# This is the URL of the n8n Trigger Webhook node.
# Streamlit will POST user messages to this URL.
N8N_WEBHOOK_IN_URL = os.getenv(
    "N8N_WEBHOOK_IN_URL",
    "https://primary-production-b8a0.up.railway.app/webhook/mvp-streamlit-chatbot"  
)

# This is optional.
# Only used if n8n returns a job_id and you need to fetch the final result later.
# If your n8n workflow responds immediately (most common case),
# you will NOT use this.
N8N_WEBHOOK_OUT_URL = os.getenv(
    "N8N_WEBHOOK_OUT_URL",
    "https://your-n8n-instance.com/webhook/chat_out"  # Optional
)

# Network settings
N8N_REQUEST_TIMEOUT = float(os.getenv("N8N_REQUEST_TIMEOUT", "60"))
N8N_POLL_INTERVAL = float(os.getenv("N8N_POLL_INTERVAL", "1.0"))
N8N_MAX_WAIT_SECONDS = float(os.getenv("N8N_MAX_WAIT_SECONDS", "60"))
