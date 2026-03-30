'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: "your api" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=what%20is%20the%20latest%20temp'

'''

import requests
import streamlit as st

def generate_ai_response(prompt: str) -> str:
    '''
    Generate AI response from the given prompt using the GenAI API. 
    
    '''
    
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {'query': prompt}
    headers={'X-API-KEY': 'your api'}
    response = requests.post(url, headers=headers, data=data)   
    response.raise_for_status()
    return response.json()


st.title("FirstGPT")

text = st.text_input("Enter your prompt here:")
if text:
    result = generate_ai_response(text)
    st.write(result)
