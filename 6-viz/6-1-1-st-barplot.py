import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt # plotting library
pengo = sns.load_dataset("penguins")
pengo['count'] = 1 # add a count column for aggregation

st.dataframe(pengo)
figure, series1 = plt.subplots() 
# create a Matplotlib figure and a set of axes series1
# the figure is the top-level container for all plot elements
# the axes is the area on which data is plotted
sns.barplot(data=pengo, x="species", 
            y="flipper_length_mm", 
            hue="sex", 
            estimator="mean",
            ax=series1).set_title("Total Count by Species")
st.pyplot(figure) # use the Streamlit function to render the plot
