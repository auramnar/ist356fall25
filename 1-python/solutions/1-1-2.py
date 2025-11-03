# Code Challenge 1-1-2
'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''

check = float(input("amount of a restaurant check: "))
tip = float(input("tip % "))
people = int(input("Number of People "))

total = check + (check*(tip/100)) 
perperson = total/people

print(f"the total is {total} and each person pays {perperson} ")
