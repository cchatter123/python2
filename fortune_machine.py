# FILE NAME - fortune_machine.py

# NAME: Oliver Doty
# DATE: 3/28/2025
# BRIEF DESCRIPTION:  Outputs random fortunes that users input



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


import random

#########################################
#               YOUR JOB:               #
#                                       #
# 1. Provide a welcome message          #
#                                       #
# 2. Create a list and populate it with #
#    the function "get_fortunes()"      #
#                                       #
# 3. Keep dispensing fortunes until the #
#    user has had enough                #
#                                       #
# 4. Thank the user.                    #
#                                       #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########
count = 0
fortunes = []
random.seed()
print("=======================================")
print("Welcome to the Fortune Telling Machine!")
print("=======================================\n\n")
print('Enter some fortunes. Type "DONE" when you are through.')
while True:
    user_input = input("Enter a fortune: ")
        
        # If the input is "DONE", break out of the `while`` loop
    if user_input == "DONE":
        random_number = random.randint(1, count)
        print()
        print(fortunes[random_number - 1])
        break
    else:
            # Otherwise, convert the input to an `int` and append
            # it to the list called `numbers`
        fortunes.append(user_input)
        count += 1

while True:
    print()
    answer = input("Another fortune (y/n)? ")

    if answer == "y":
        random_number = random.randint(1, count)
        print(fortunes[random_number - 1])
    else:
        print("\n\nThank you for using the Fortune Telling Machine!\nSmash that LIKE and Subscribe button and tell your friends!")
        break



########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
=======================================
Welcome to the Fortune Telling Machine!
=======================================


Enter some fortunes. Type "DONE" when you are through.
Enter a fortune: You will live a long life.
Enter a fortune: You will be rich!
Enter a fortune: You will eat the most delicious cookie later this week.
Enter a fortune: You have a great smile.
Enter a fortune: DONE

You will live a long life.

Another fortune (y/n)? y
You will eat the most delicious cookie later this week.

Another fortune (y/n)? y
You will live a long life.

Another fortune (y/n)? y
You will be rich!

Another fortune (y/n)? y
You will eat the most delicious cookie later this week.

Another fortune (y/n)? y
You will be rich!

Another fortune (y/n)? n


Thank you for using the Fortune Telling Machine!
Smash that LIKE and Subscribe button and tell your friends!
'''


'''
=======================================
Welcome to the Fortune Telling Machine!
=======================================


Enter some fortunes. Type "DONE" when you are through.
Enter a fortune: a
Enter a fortune: b
Enter a fortune: c
Enter a fortune: DONE

c

Another fortune (y/n)? y
a

Another fortune (y/n)? y
a

Another fortune (y/n)? y
c

Another fortune (y/n)? y
c

Another fortune (y/n)? y
b

Another fortune (y/n)? y
b

Another fortune (y/n)? n


Thank you for using the Fortune Telling Machine!
Smash that LIKE and Subscribe button and tell your friends!
'''


'''
=======================================
Welcome to the Fortune Telling Machine!
=======================================


Enter some fortunes. Type "DONE" when you are through.
Enter a fortune: You smell funny.
Enter a fortune: You smell awesome!
Enter a fortune: Watch out for falling ice cream.                  
Enter a fortune: Enjoy your time in the fields of gold!
Enter a fortune: This is the clock song.
Enter a fortune: Cold comfort for change.
Enter a fortune: DONE

Cold comfort for change.

Another fortune (y/n)? y
Cold comfort for change.

Another fortune (y/n)? y
Enjoy your time in the fields of gold!

Another fortune (y/n)? y
This is the clock song.

Another fortune (y/n)? n


Thank you for using the Fortune Telling Machine!
Smash that LIKE and Subscribe button and tell your friends!
'''




########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?

Getting the output correct and gettings things to output/append correctly





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
[x] I'm solid. Totally got it.

'''