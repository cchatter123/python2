# FILE NAME - dice.py

# NAME: Oliver Doty
# DATE: 2/25/2025
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########



seed_from_user = int(input("Enter a seed for the random number generation: "))
random.seed(seed_from_user)
random_number = random.randint(1, 6)
random_number2 = random.randrange(1, 7)
print(f'Die roll one is {random_number}')
print(f'Die roll two is {random_number2}')






########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?






'''



