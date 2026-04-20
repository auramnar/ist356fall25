#Code Challenge 1-1-1¶
#Write a program to input your first name and last name then output your last name, first name

x = input("Full name: ")
name = x.split()
reverse_name = name[::-1]
reverse_output = ' '.join(reverse_name)
print(reverse_output)


