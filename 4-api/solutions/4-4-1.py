
#url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"

from fastapi import FastAPI, Query
import pandas as pd
import numpy as np
import json

app = FastAPI()

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df =pd.read_csv(url)

@app.get("/api/search_flights")
def search_flights(type:str =Query(), code:str = Query()):
    if type == "dep":
        flights = df[df['departure_airport_code'] == code]
    elif type == "arr":
        flights= df[df['arrival_airport_code'] == code]
    else:
        return {}

    json_flights = flights.to_json(orient='records') # string
    return json.loads(json_flights)  # list of dicts


        
    

