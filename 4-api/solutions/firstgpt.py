import requests
import streamlit as st

def get_text_completion(query: str) -> str:
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query": query }
    headers = {"X-API-KEY": "your_api_key_here"}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()
    
st.title("First GPT App")
text = st.text_input("Enter a prompt to send to the AI model")
response = get_text_completion(text)
st.write(response)
