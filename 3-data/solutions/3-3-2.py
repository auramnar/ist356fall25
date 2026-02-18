import streamlit as st
import pandas as pd
import requests
import numpy as np

# march_purchases = pd.read.csv(f"{base}/purchases-mar.csv" )


'''
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
customers = pd.read_csv(f"{base}/customers.csv")
st.dataframe(customers)
march_purchases = pd.read_csv(f"{base}/purchases-mar.csv")
st.dataframe(march_purchases)


months = ['jan', 'feb', 'mar', 'apr']
months_dfs = []
for month in months:
    month_df = pd.read_csv(f"{base}/purchases-{month}.csv")
    month_df['month'] = month # add lineage to the dataframe (e.g. add the month name)
    months_dfs.append(month_df) # add the dataframe to a list of months     
all_purchases = pd.concat(months_dfs) # concat the list of months together one dataframe
st.dataframe(all_purchases) # print dataframe  
combined = pd.merge(customers, all_purchases, on='customer_id', how='left') # merge customers with purchases
st.dataframe(combined) # print combined dataframe

select_month = st.selectbox("Select a month", options=['jan', 'feb', 'mar', 'apr'])
cols_to_show = ['customer_id', 'firstname', 'lastname']
did_not_buy = combined["order_id"].isnull()
customers_who_did_not_buy = combined[did_not_buy][cols_to_show]

'''

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

st.title("Who's not Buying from MiniMart?")
month = st.selectbox('Select Month:', months)

purchases = pd.read_csv(f"{base}/purchases-{month}.csv")

# Code here...

customers = pd.read_csv(f"{base}/customers.csv")
combined = pd.merge(customers, purchases, left_on='customer_id', right_on= 'customer_id', how='left')
st.dataframe(combined)
cols= ['customer_id', 'firstname', 'lastname']
did_not_buy = combined["order_id"].isnull()
customers_who_did_not_buy = combined[did_not_buy][cols]

st.dataframe(customers_who_did_not_buy, hide_index=True)
