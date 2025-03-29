# FILE NAME - password_strength_analyzer.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random


########## ENTER YER CODE BELOW THIS LINE ##########




import re 

password = input("Enter your password: ")

length = len(password)
lowercase = sum(c.islower() for c in password)
uppercase = sum(c.isupper() for c in password)
digits = sum(c.isdigit() for c in password)
spec = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
length_score = 0
upper_score = 0
lower_score = 0
digit_score = 0
special_score = 0
total_score = 0

if length>=15: length_score=8
elif length>=8: length_score=5 
total_score += length_score

if lowercase>2: lower_score=8
elif lowercase==2: lower_score=4
elif lowercase==1: lower_score=2
total_score += lower_score

if uppercase>2: upper_score=8
elif uppercase==2: upper_score=4
elif uppercase==1: upper_score=2
total_score += upper_score

if digits>2: digit_score=8
elif digits==2: digit_score=4
elif digits==1: digit_score=2
total_score += digit_score

if spec>2: special_score=8
elif spec==2: special_score=4
elif spec==1: special_score=2
total_score += special_score

print()
print("Password Analysis Report")
print("-------------------------")
print(f'LENGTH: {length_score} points ({length} characters)')
print(f'UPPERCASE: {upper_score} points ({uppercase} uppercase letter(s))')
print(f'LOWERCASE: {lower_score} points ({lowercase} lowercase letter(s))')
print(f'NUMBERS: {digit_score} points ({digits} number(s))')
print(f'SPECIAL CHARACTERS: {special_score} points ({spec} special character(s))')
print()

print("Total Score:", total_score/40)
print(f'Strength Percentage: {(total_score/40)*100}%')




########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
Enter your password: password

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 0 points (0 uppercase letter(s))
LOWERCASE: 8 points (8 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.325
Strength Percentage: 32.5%
'''

'''
Enter your password: p@$$WORD

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 8 points (4 uppercase letter(s))
LOWERCASE: 2 points (1 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.575
Strength Percentage: 57.49999999999999%
'''

'''
Enter your password: 123PASwor

Password Analysis Report
-------------------------
LENGTH: 5 points (9 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.725
Strength Percentage: 72.5%
'''

'''
Enter your password: 123pasWOR!@#

Password Analysis Report
-------------------------
LENGTH: 5 points (12 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.925
Strength Percentage: 92.5%
'''

'''
Enter your password: 123pasWOR!@#888888888888

Password Analysis Report
-------------------------
LENGTH: 8 points (24 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (15 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 1.0
Strength Percentage: 100.0%
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?







'''



########################################
#            ATTESTATION
########################################

'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''