# FILE NAME - random_seeded_number.py

# NAME: Oliver Doty
# DATE: 2/25/2025
# BRIEF DESCRIPTION:  Outputs a random number based on the seed given by the user



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


seed_from_user = int(input("Enter a seed for the random number generation: "))
random.seed(seed_from_user)
random_number = random.random()
print(random_number)







########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
0.5703284231368732

'''



'''

Enter a seed for the random number generation: 0
0.8444218515250481

'''



'''

Enter a seed for the random number generation: 10
0.5714025946899135

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. In your own words, explain what "seeded" means (for instance, "seeding a random number generator").


It is a number that has preset generated outputs. So lets say your seed is 5, 5 will have a different random number output than 6




'''



