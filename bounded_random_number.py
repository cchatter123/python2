# FILE NAME - bounded_random_number.py

# NAME: Oliver Doty
# DATE: 2/25/2025
# BRIEF DESCRIPTION:  outputs a number between 1-10 based on the seed given by the user



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
    
  
########## ENTER YER CODE BELOW THIS LINE ##########





seed_from_user = int(input("Enter a seed for the random number generation: "))
random.seed(seed_from_user)
random_number = random.randint(1, 10)
print(random_number)




########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
10

'''



'''

Enter a seed for the random number generation: 32
2

'''



'''

Enter a seed for the random number generation: 100
3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is a good way to remember if the arguments (parameters) for a bounded number are inclusive or exclusive?






'''



