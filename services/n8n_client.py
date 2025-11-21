# services/n8n_client.py
import requests
from typing import Any, Dict

from config.settings import (
    N8N_WEBHOOK_IN_URL,
    N8N_REQUEST_TIMEOUT,
)


def _extract_text_from_payload(payload: Dict[str, Any]) -> str:
    """
    Try to extract the message text from different common keys.
    Fallback: convert full payload to string.
    """
    for key in ("answer", "reply", "message", "content", "text"):
        if key in payload and isinstance(payload[key], str):
            return payload[key]

    return str(payload)


def send_message_to_n8n(prompt: str, session_id: str) -> str:
    """
    Send the user prompt to the n8n Webhook Trigger.
    Expect a synchronous final response from 'Respond to Webhook'.

    Parameters:
        prompt (str): user message
        session_id (str): unique session identifier

    Returns:
        str: assistant final answer from n8n
    """
    payload = {
        "session_id": session_id,
        "message": prompt,
    }

    response = requests.post(
        N8N_WEBHOOK_IN_URL,
        json=payload,
        timeout=N8N_REQUEST_TIMEOUT,
    )

    # Raise exception if HTTP error (4xx, 5xx)
    response.raise_for_status()

    try:
        data = response.json()
    except ValueError:
        # n8n returned plain text
        return response.text

    return _extract_text_from_payload(data)
