# Streamlit + Chatbot (MVP)

Lightweight Streamlit frontend to chat with a single n8n flow. The app renders one chat page, sends the user message to one webhook, and displays the reply. All memory/AI happens in n8n; Streamlit only handles the interaction.

## MVP Scope
- Single endpoint: n8n inbound webhook (`N8N_WEBHOOK_IN_URL`).
- Single role: end user (n8n replies as assistant).
- Single flow: linear conversation, no branches.
- Single interaction type: text (`st.chat_input`).
- Single uploader/admin: no upload UI in Streamlit; if enabled, it would be handled by n8n.
- One-page UI: `app.py` with history, input, and reset button.

## Quick Architecture
- Streamlit renders the UI and keeps `session_state` (`session/state_manager.py`).
- Messages go to n8n via `services/n8n_client.py` (POST JSON with `session_id` and `message`).
- Streaming effect simulated with `services/stream_utils.py`.
- Layout and styles: `ui/layout.py`, `ui/components.py`, `styles/theme.css`.

## Requirements
- Python 3.10+ recommended.
- Install deps: `pip install -r requirements.txt`.

## Configuration
1) Copy environment variables (optional): rename `.env.example` or export in your shell.
2) Set the n8n webhook (required for production):
   - `N8N_WEBHOOK_IN_URL`: Trigger Webhook URL that receives `{ session_id, message }`.
   - Optional: `N8N_REQUEST_TIMEOUT` to tune timeout (default 60s).

Other keys in `.env.example` (Supabase, upload) are not used in this MVP; they are reference if you extend the n8n flow.

## Local Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
Open the link Streamlit prints (default `localhost:8501`).

## Usage Flow
1) Type a message in the chat box.
2) Streamlit stores history in session and POSTs to the n8n webhook with `session_id`.
3) n8n returns the final reply; the UI renders it with a typewriter effect.
4) "Clear Chat" wipes history and keeps you on the same page.

## Folder Structure
- `app.py`: entrypoint and only page.
- `config/settings.py`: title/icon and n8n webhook URL.
- `services/`: HTTP client to n8n and streaming helpers.
- `session/`: session state helpers.
- `ui/` and `components/`: layout, sidebar, message rendering.
- `styles/`: CSS theme.

## Quick Deploy
- Push the repo to your Streamlit/containers hosting.
- Set `N8N_WEBHOOK_IN_URL` in the deployment environment.
- Ensure n8n responds synchronously to the webhook (this MVP expects an immediate response).

## Next Steps (optional)
- Add auth (token or login).
- Add file upload if your n8n flow consumes documents.
- Handle async/queued responses if the backend stops being synchronous.
