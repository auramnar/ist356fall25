"""curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=what'\''s%20the%20weather%20in%20syracuse'"""

import request 
import streamlit as st

def open_api_call(prompt: str) -> str:

    url = "https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000"
    data {"query": prompt}
    headers=("X-API-key": "86c3c24b1deac9ab06294bd6")
    response = requests.post(url headers=headers, data=data)
    response.raise_for_stats()
    return reponse.json()

def spellcheck(text):
    prompt =f"Please spellcheck the following text: {text}"
    prompt += 'text + /n'
    prompt += "for each mistakem provid the correct"
    
    result = open_api_call(prompt)
    st.write(result)

st.title("spellchecker using LLM")
text = st.text_area 