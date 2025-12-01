'''
Create a streamlit with the fast food dataset. 

`fast_food_nutrition_cleaned.csv` 

Let' input the macro nutrient: protein, fat, carbs, and sugar as a dropdown.

Create a heatmap of the calories vs. the macro nutrient broken down by the type fast food restaurant.

You'll have to pivot the data to create the heatmap. So use a mean aggregation to create the heatmap... average carbs, etc...

How can you interpret the heatmap you see?

'''



import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)

companies = sorted(list(ff['company'].unique()))
print(companies)

value = st.selectbox("Select Macronutrient", ['fat_g', 'carbs_g', 'sugars_g', 'protein_g', 'sodium_mg'])

ffp = ff.pivot_table(index='company', columns='calories',values=value, aggfunc=np.mean)

figure, series1 = plt.subplots(figsize=(20, 15))
sns.heatmap(
    ffp, 
    ax=series1, 
    cmap="YlOrRd",      # 🔥 Heat-style palette (good for nutrients)
    linewidths=.3, 
    annot=False)
st.pyplot(figure)
