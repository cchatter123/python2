# FILE NAME - sum_values.py

# NAME: Oliver Doty
# DATE: 3/28/2025
# BRIEF DESCRIPTION:  



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

login_count = 0
print("Please enter failed login attempts")
print("==================================\n")


day = int(input("  Monday:    "))
login_count += day
day = int(input("  Tuesday:   "))
login_count += day
day = int(input("  Wednesday: "))
login_count += day
day = int(input("  Thursday:  "))
login_count += day
day = int(input("  Friday:    "))
login_count += day
print("\n")
print("===== FAILED LOGIN ATTEMPTS ANALYZER =====\n")
print(f'Total failed login attempts for the week: {login_count}\n')

if login_count >= 100:
    print("SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!\nRecommendation: Investigate for potential brute force attacks.")
else:
    print("Everything seems normal. It's quiet. Too quiet.\nRecommendation: Continue routine monitoring.")



########### END YER CODE ABOVE THIS LINE ###########
    




########################################
#          SAMPLE OUTPUT
########################################

'''
Please enter failed login attempts
==================================

  Monday:    1
  Tuesday:   2
  Wednesday: 3
  Thursday:  4
  Friday:    5


===== FAILED LOGIN ATTEMPTS ANALYZER =====

Total failed login attempts for the week: 15

Everything seems normal. It's quiet. Too quiet.
Recommendation: Continue routine monitoring.
'''


'''
Please enter failed login attempts
==================================

  Monday:    12
  Tuesday:   10
  Wednesday: 4
  Thursday:  0
  Friday:    88


===== FAILED LOGIN ATTEMPTS ANALYZER =====

Total failed login attempts for the week: 114

SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!
Recommendation: Investigate for potential brute force attacks.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you sum the element in the list?


after each input I just added them together into a int value




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