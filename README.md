# Agentic AI Personal Assistant (Streamlit + n8n)

An **Agentic AI Personal Assistant** that pairs a lightweight **Streamlit** UI with an **n8n** automation backend to orchestrate real-world actions through multiple tools.

The assistant is designed for **multi-tool orchestration** across Google Workspace and web utilities, including:

- Gmail (read/send/reply, triage)
- Google Calendar (create/update events, availability checks)
- Google Docs (drafting and summarization workflows)
- Google Sheets (logging, planning, simple reporting)
- Web Search (lookup + enrichment)

> **Frontend**: Streamlit (`app.py`)  
> **Backend**: n8n workflows (triggered via webhook)  
> **AI**: Cohere (or your preferred LLM provider) embedded within n8n

---

## Features

- **Agentic workflow execution**
  - Send a single instruction and let the backend agent decide which tools to use.
- **Multi-tool orchestration**
  - Compose actions across Gmail, Calendar, Docs, Sheets, and Web Search.
- **Human-in-the-loop ready**
  - Streamlit UI is a natural place for confirmations, previews, and approvals.
- **Separation of concerns**
  - Streamlit handles interaction; n8n handles automation + integrations.

---

## Architecture

This project follows a simple, production-friendly split:

- **Streamlit Frontend**
  - Collects user intent (prompts/commands)
  - Sends requests to n8n via a webhook URL (`N8N_WEBHOOK_URL`)
  - Displays results and statuses

- **n8n Backend (Agent + Tools)**
  - Receives webhook events from Streamlit
  - Routes requests through an agentic decision layer
  - Calls external tools/integrations (Google Workspace, search, etc.)
  - Returns structured output back to the Streamlit UI

---

## Prerequisites

- **Python 3.10+**
- **n8n** instance (self-hosted or cloud)
- **Cohere API key** (or whichever LLM provider your n8n agent workflow uses)
- Google Workspace credentials configured inside n8n (as needed for Gmail/Calendar/Docs/Sheets)

---

## Setup Instructions

1. **Clone the repository**

2. **Create and activate a virtual environment**

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   - Copy `.env.example` to `.env`
   - Set your n8n webhook URL:

   ```env
   N8N_WEBHOOK_URL=https://your-n8n-instance/webhook/your-trigger
   ```

5. **Add your n8n workflow export**

   - Export your workflow from n8n
   - Paste it into `n8n_workflow.json`

6. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## Repository Contents

- `app.py` - Streamlit frontend
- `n8n_workflow.json` - Placeholder for the exported n8n workflow JSON
- `.env.example` - Environment variable template
- `requirements.txt` - Python dependencies

---

## License

Add a license if you plan to distribute this publicly.
