import pandas as pd
import numpy as np
import requests
import streamlit as st

# online_students.rename(columns={"Name": "StudentName"}, inplace=True)

'''
for each department:
    create a dataframe for that department (e.g. from the json under the department)
    add lineage to the dataframe (e.g. add the department name)
    add the dataframe to a list of departments
concat the list of departments together one dataframe
print dataframe

df_list = []
for key in employees.keys():
    df = pd.DataFrame(employees[key])
    df['department'] = key
    df_list.append(df)
combined_df = pd.concat(df_list)
st.dataframe(combined_df)



df = pd.DataFrame(employees['accounting'])
st.dataframe(df)

'''


link ="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(link)
employees = response.json()
st.write(employees) # this will show the dictionary

departments=[]
for dept_name in employees.keys():
    dept_employees = pd.json_normalize(employees, record_path=dept_name)
    st.write(dept_employees)
    dept_employees['dept'] = dept_name
    departments.append(dept_employees)
    
combined = pd.concat(departments, ignore_index=True)

st.dataframe(combined)


