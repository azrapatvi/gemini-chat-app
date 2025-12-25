import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 Gemini Chatbot")

# Initialize Gemini chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for role, msg in st.session_state.messages:
    with st.chat_message(role.lower()):
        st.markdown(msg)

# Chat input (best for Streamlit)
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(("User", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Gemini response
    response = st.session_state.chat.send_message(user_input)

    st.session_state.messages.append(("Assistant", response.text))
    with st.chat_message("assistant"):
        st.markdown(response.text)
