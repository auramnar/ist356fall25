'''
Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

1. the data in a dataframe 
2. select a category: gender or operating system
3. select a measure: Data useage, battery drain, screen on time, or app useage time
4. show a bar plot of the average of 3. by 2.


'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

