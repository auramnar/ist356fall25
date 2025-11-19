'''
Create a streamlit with a histogram of the calories column in the fast food dataset.

`fast_food_nutrition_cleaned.csv` 

the input is the number of bins as a slider. between 1 and 100 bins.

What happens to the data shape when you increase the number of bins?

'''

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
#print(ff.columns)

bins = st.slider("Select the number of bins", min_value=1, max_value=100)
st.write(f"Number of bins: {bins}")
figure, series1 = plt.subplots()
sns.histplot(data=ff, x="calories", bins=bins, kde=True, ax=series1).set_title("Calories Histogram")
st.pyplot(figure)


st.dataframe(ff)
