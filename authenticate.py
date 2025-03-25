# FILE NAME - authenticate.py

# NAME: Oliver Doty
# DATE: 3/25/2025
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

password = input("Enter password: ")
correct = "tooManySecrets"
print()

while password != correct:
    print("Password does not match.")
    password = input("Enter password:")
    print()

print("Access granted.")


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter password: a

Password does not match.
Enter password: b

Password does not match.
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: toomanysecrets

Password does not match.
Enter password: TOOMANYSECRETS

Password does not match.
Enter password: too_Many_Secrets

Password does not match.
Enter password: tooManySecrets

Access granted.
'''

