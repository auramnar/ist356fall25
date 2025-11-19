import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
st.dataframe(mobile)

