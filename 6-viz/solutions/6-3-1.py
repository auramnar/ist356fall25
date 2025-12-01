import pandas as pd
import streamlit as st
import folium
import streamlit_folium as sf


days  = {
    'Sunday': 'red',
    'Monday': 'orange',
    'Tuesday': 'beige',
    'Wednesday': 'green',
    'Thursday': 'blue',
    'Friday': 'purple',
    'Saturday': 'gray'
}

st.title('Streamlit Park magic')

map = folium.Map(location=[43.0481, -76.1474], zoom_start=15) # create a folium map centered at Syracuse
df = pd.read_csv('./6-viz/data/final_cuse_parking_violations.csv')
df_dropped = df.dropna() # remove rows with missing data
status = df_dropped['status'].unique() # extract all unique status values

status = st.selectbox('Select ticket status: ', status) # create a dropdown for status

df_filtered = df_dropped[df_dropped['status'] == status] # filter dataframe based on status

df_sample = df_filtered.sample(10) 

