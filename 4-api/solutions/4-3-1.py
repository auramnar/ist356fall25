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

#WRAP THE OPEN AI IN A FUNCTION
def generate_ai_response(prompt: str) -> str:
    '''
    Generate AI response from the given prompt using the GenAI API. 
    
    '''
    #params = {'temperature': 0}
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {'query': prompt}
    headers={'X-API-KEY': 'your api'}
    response = requests.post(url, headers=headers, data=data, params = params)   
    response.raise_for_status()
    return response.json()

#check = generate_ai_response("Are you smart")
#st.write(check)
# FOR EACH PROMPT YOU ENGINEER MAKE A FUNCTION
# SO YOU CAN CREATE DIFFERNT VERSIONS AND EVALUATE
def spellcheck(text):
  prompt = "Spell check the following text"
  prompt += text "\n"
  prompt += text + "\n"
  prompt += "for each misspelling provide one suggestion"
  #prompt += "return as a list of dictionaries in JSON format"
  check = generate_ai_response(prompt)
  return check

#MAIN PROGRAM
st.title("SPELL CHECKER")
text = st.text_area("Enter text")
s_check = spellcheck(text)
st.write(s_check)


  
st.title("FirstGPT")

text = st.text_input("Enter your prompt here:")
if text:
    result = generate_ai_response(text)
    st.write(result)
