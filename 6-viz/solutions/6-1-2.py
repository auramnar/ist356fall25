import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

category = st.selectbox("Select Category", ["Age", "Operating System"])
quantity = st.selectbox("Select Measure", 
                        ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hours/day)", "App Usage Time (hours/day)"])

figure,series1 =plt.subplots()
sns.lineplot(data=mobile, x=category, y=quantity, estimator= 'mean', ax=series1)
st.pyplot(figure)