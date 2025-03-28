# FILE NAME - pop_and_insert.py

# NAME: Oliver Doty
# DATE: 3/27/2025
# BRIEF DESCRIPTION:  Takes an input and moves the first inputted name to the end of the list 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience








#########################################
#               YOUR JOB:               #
#                                       #
# 1. Move the first item in the list to #
#    be the last item                   #
#                                       #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########


customers = []


driver_name = ''

while driver_name != 'EOF':
    driver_name = input("Enter the name of the customer: ")


    if driver_name != "EOF":
        customers.append(driver_name)

print()


print(customers)
first_name = customers.pop(0)
customers.append(first_name)
print(customers)








########### END YER CODE ABOVE THIS LINE ###########
    




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the name of the customer: Alice
Enter the name of the customer: Bob
Enter the name of the customer: Charlie
Enter the name of the customer: Danielle
Enter the name of the customer: EOF

['Alice', 'Bob', 'Charlie', 'Danielle']
['Bob', 'Charlie', 'Danielle', 'Alice']
'''


'''
Enter the name of the customer: Eliza
Enter the name of the customer: EOF

['Eliza']
['Eliza']
'''


'''
Enter the name of the customer: 1234
Enter the name of the customer: 2345
Enter the name of the customer: 3456
Enter the name of the customer: 4567
Enter the name of the customer: EOF

['1234', '2345', '3456', '4567']
['2345', '3456', '4567', '1234']
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you move the element in the list?


After outputting the original list I popped the first element and then reappended it then printed the new list




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