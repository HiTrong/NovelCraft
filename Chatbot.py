# ====== Import Libraries ======
from API_handle import get_gemini_response
from prompt_templates import get_chatbot_prompt
import streamlit as st

# ====== Chatbot ======
def get_chatbot_response(api_key, human_input, lang):
    prompt = get_chatbot_prompt(human_input, lang)
    response = get_gemini_response(api_key, prompt, lambda: st.warning("Please check your API and content moderation. Something went wrong!"))
    if response is None: return "Please try again later!"
    return response