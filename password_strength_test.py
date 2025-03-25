# FILE NAME - password_strength_test.py

# NAME: Oliver Doty
# DATE: 3/25/2025
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
import re 

print("===== PASSWORD STRENGTH CHECKER =====")
print("This tool analyzes your password and rates its strength.\n")
password = input("Enter a password to check: ")

length = len(password)
lowercase = sum(c.isupper() for c in password)
uppercase = sum(c.islower() for c in password)
digits = sum(c.isdigit() for c in password)
spec = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))

print()
print("===== PASSWORD ANALYSIS =====")
print(f'Length: {length} characters')
print(f'Uppercase letters: {uppercase}')
print(f'Lowercase letters: {lowercase}')
print(f'Digits: {digits}')
print(f'Special characters: {spec}')
print()
score = 0
diversity = 0

if length >=12: score += 25
elif length >=8: score += 15
elif length >=6: score +=10
else: score+= 0

if lowercase >=1:
     score += 15
     diversity += 1
if uppercase >=1:
     score += 15
     diversity += 1
if digits >=1:
     score += 15
     diversity += 1
if spec >=1:
     score += 15
     diversity += 1

if diversity >= 3:
     score += 15


print(f'Security Score: {score}/100')
if score >= 80: print("Strength Assessment: STRONG")
elif score >= 60: print("Strength Assessment: MODERATE")
elif score >= 40: print("Strength Assessment: WEAK")
else: print("Strength Assessment: VERY WEAK")
print()


print("===== IMPROVEMENT SUGGESTIONS =====")
if length<12: print("- Use at least 12 characters for better security")
if uppercase<1: print("- Add uppercase letters (A-Z)")
if lowercase<1: print("- Add lowercase letters (A-Z)")
if digits<1: print("- Add numbers (0-9)")
if spec<1: print("- Add special characters (!@#$%^&*)")


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: password

===== PASSWORD ANALYSIS =====
Length: 8 characters
Uppercase letters: 0
Lowercase letters: 8
Digits: 0
Special characters: 0

Security Score: 30/100
Strength Assessment: VERY WEAK

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Add special characters (!@#$%^&*)
'''


'''
This tool analyzes your password and rates its strength.

Enter a password to check: p@SSword!

===== PASSWORD ANALYSIS =====
Length: 9 characters
Uppercase letters: 2
Lowercase letters: 5
Digits: 0
Special characters: 2

Security Score: 75/100
Strength Assessment: MODERATE

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add numbers (0-9)
'''


'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: 4$DL_dsa_dsf!#

===== PASSWORD ANALYSIS =====
Length: 14 characters
Uppercase letters: 2
Lowercase letters: 6
Digits: 1
Special characters: 5

Security Score: 100/100
Strength Assessment: STRONG

===== IMPROVEMENT SUGGESTIONS =====
- Excellent password! Remember to use different passwords for different accounts.
'''
