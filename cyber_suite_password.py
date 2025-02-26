# FILE NAME - password.py

# NAME: Oliver Doty
# DATE: 2/25/2025
# BRIEF DESCRIPTION:  Uses a user given seed to give you a random generated password



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
import string
  
########## ENTER YER CODE BELOW THIS LINE ##########


user_seed = int(input("Enter a seed for the random number generation: "))

random.seed(user_seed)

randChar = random.choice("!@#$&(),-_")

randLow = random.choice(string.ascii_lowercase)
randUp = random.choice(string.ascii_uppercase)

randLow2 = random.choice(string.ascii_lowercase)
randUp2 = random.choice(string.ascii_uppercase)

randNum = random.choice(string.digits)
randNum2 = random.choice(string.digits)

randChar2 = random.choice("!@#$&(),-_")

print("Your random password is: ")
print(f'{randChar}{randLow}{randUp}{randLow2}{randUp2}{randNum}{randNum2}{randChar2}')








########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

I kept messing up the order of the outputs that honestly was my struggle




2. What value do you see in the `string` module?






'''



