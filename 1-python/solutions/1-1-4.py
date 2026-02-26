# Code Challenge 1-1-4¶
'''
Number to Letter grade
Letter grades in a college class are computed as follows:

95 and above is an A
75 and above, but below 95 is a B
50 and above, but below 75 is a C
below 50 is F
Write a program to input the number grade and calculate the letter grade

Re-write to account for "bad" grades > 120 or < 0
'''


grade = float(input("What is your grade? "))
if grade >= 95: 
    print("A")
elif grade <95 and grade >= 75: 
    print("B")
elif grade <75 and grade >=50:
    print("c")
elif grade <50:
    print("F")
elif grade >100 and grade <0: 
    print("Please input a grade between 0-100")




