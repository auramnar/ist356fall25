'''
write a program to read in a string of students and gpas in one input statement 

Suggested approach:

    1. input text
    2. for each student split on "," from the text
    3.    split the student into name and gpa 
    4.    parse the gpa so its a float
    5.    add the name and gpa to the list
    6. write the list to students.json as JSON




'''

# Import modules 
import json
import os # python utility for creating file paths

folder_name = "1-python/data" # directory where the json file will be saves


text = input("Enter names and grades: ")
students = [] # store data as a dictionary
for student in text.split(","): # split on comma creating smaller strings
    name, grade = student.strip().split() # tuple unpacking. remove spaces and split by spaces
    grade = float(grade)
    students.append({"name": name, "grade": grade}) # create a dictionary and add to students list

file_path = os.path.join(folder_name, "students.json")  # is used instead of manually typing / so it works across operating systems.
# "1-python/data/students.json"

with open(file_path, "w") as file:
    json.dump(students, file) # write to file in json format
