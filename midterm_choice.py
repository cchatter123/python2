# FILE NAME - midterm_choice.py

# NAME: Oliver Doty
# DATE: 4/9/2025
# BRIEF DESCRIPTION:  gives the user a choice to pick rectangle or circle to find its area then computes it



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

print("Welcome to the Mathenator2000\n")

print("Please choose from the following menu:\n  1. Compute area of a circle\n  2. Compute area of the rectangle\n")
answer = int(input("What is your choice? "))
print()
if answer == 1:
    radius = float(input("What is the radius of a circle? "))
    print(f'The area of the circle is {(radius * radius) * 3.14}')
elif answer == 2:
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    print(f'The area of the rectangle is {length * width}')
else: 
    print("Invalid selection.")

print()
print("Thank you for using the Mathinator2000")