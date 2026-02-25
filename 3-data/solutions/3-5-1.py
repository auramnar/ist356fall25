
'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection

'''
import pandas as pd
import streamlit as st



url ='https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'





st.title ('Exam Scores Summary')

options = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups'] # list will be a dropdown menu
exams = pd.read_csv(url) # load exam date 
option =st.selectbox('Select an option', options) # dropdown menu

summary = exams.groupby(option).agg({'Class_Section': 'count', 'Student_Score':'mean'})
# group the dataframe by the strategy selected in option 
# reset index to turn the groupby index into a column
# Counts students in each group
# Averages the student scores in each group

# reset index to turn the groupby index into a column
summary = summary.reset_index()
#summary = summary.rename(columns = {'Class_Section':'Student_Count', 'Student_Score':'Average Score'}) 

st.dataframe(summary)
