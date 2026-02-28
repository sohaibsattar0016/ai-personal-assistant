import streamlit as st
import requests
import os
from dotenv import load_dotenv

# .env file se variables load karne ke liye
load_dotenv()

# --- CONFIGURATION ---
# Ab URL directly .env file se aayega
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Sohaib's AI Assistant",
    page_icon="⚡",
    layout="centered"
)

# --- SIDEBAR (MY SERVICES) ---
with st.sidebar:
    st.title("⚡ My Assistant")
    st.markdown("Your personal Agentic AI command center.")
    
    st.divider()
    st.markdown("### 🛠️ Active Capabilities")
    st.markdown("""
    - 📧 **Gmail:** Read, summarize, and send emails.
    - 📅 **Calendar:** Book and check my schedule.
    - 💰 **Expenses:** Log and calculate my spending.
    - 📝 **Docs & Notes:** Manage my Google Docs.
    - 🌍 **Web Search:** Fetch live information.
    """)
    st.divider()
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- MAIN CHAT INTERFACE ---
st.title("💬 Welcome back, Sohaib")
st.markdown("What are we getting done today?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT & LOGIC ---
if prompt := st.chat_input("Ask me to schedule a meeting, check emails, or log an expense..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Executing..."):
            try:
                payload = {
                    "name": "Sohaib",
                    "message": prompt
                }
                response = requests.post(N8N_WEBHOOK_URL, json=payload)
                
                if response.status_code == 200:
                    result_data = response.json()
                    
                    if isinstance(result_data, list) and len(result_data) > 0:
                        bot_reply = result_data[0].get("output", "Task completed!")
                    elif isinstance(result_data, dict):
                        bot_reply = result_data.get("output", "Task completed!")
                    else:
                        bot_reply = f"Done! Raw response: {result_data}"
                    
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.error(f"Error connecting to AI Agent. Status code: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Failed to reach the n8n webhook. Is n8n running? Error: {e}")