import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd


# Here's a more straigtforward example with unemployment data:


CENTER_US = (39.8333333,-98.585522) # set map center
# dataset with unemployment stats
u_df = pd.read_csv('https://raw.githubusercontent.com/wrobstory/vincent/master/examples/data/US_Unemployment_Oct2012.csv')
state_geojson = './6-viz/data/us-states.geojson' # geojson file with state shapes
geo = gpd.read_file(state_geojson) # contains polygons for each state
combined = pd.merge(geo, u_df, left_on='id', right_on='State') # merge using state names
map = folium.Map(location=CENTER_US, zoom_start=4) # create a base folium map
st.write('## US Unemployment Choropleth - 2012') # title
out_map = combined.explore(m=map, column='Unemployment', cmap='YlGn', legend=True)
# .explore() creates the choropleth on the map using folium
# m=map draw the map created earlier
# column='Unemployment' use this column for coloring    
# cmap='YlGn' use this color map
# legend=True show a legend

sf.folium_static(out_map)