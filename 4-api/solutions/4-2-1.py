'''
Post curl here
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=pizza%20is%20good%20not%20customer%20service'


'''



import pandas as pd
import numpy as np
import streamlit as st
import requests
import json 



def extract_entities(text: str)->dict:
    '''
    Extract entities from the text using Azure entity recognition API.
    '''
    
# Complete function 

    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    data = {'text': text}
    headers={'X-API-KEY': 'ec25dc1e1297cfba51838bd3'}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()


text = st.text_area("Enter text to extract entities:")
# text = "I like sunny days"
#result = extract_entities(text)
#entities = result ['results']['documents'][0]['entities']
#st.write(result)
#st.write(entities)
#df = pd.DataFrame(entities)

# Complete code to call the function and display results
if st.button("Extract Entities"): # create a button

  if text: # chack if the variable text has any content
      result = extract_entities(text) # assign function to a variable
      entities = result ['results']['documents'][0]['entities'] # extract entities from the json response from nexted dictionary
      df = pd.DataFrame(entities) # convert the list of entities to a dataframe
      st.dataframe(df) # display the dataframe in streamlit
