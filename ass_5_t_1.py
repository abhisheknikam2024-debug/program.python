import re
#create a dictionary
std_mark = {
    "Raj" : 85,
    "Sahil" : 89,
    "Balu" : 95,
    "Harh" : 78
    }
#ask for user input
user_input = input("enter a student's name:").strip()
#strip() used tp clean a unwanted spaces by user 

# regular expression
student_name = user_input.title()     # title() use to mark a frist letter in upper case and another in lower case  

if student_name in std_mark:
    print(f"{student_name}'s mark:{std_mark[student_name]}")
else:
    print("student note found!")      