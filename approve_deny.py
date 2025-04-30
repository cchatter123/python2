# FILE NAME - approve_deny.py

# NAME: Oliver Doty
# DATE: 4/29/2025
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

approveFile = "approve.txt"
denyFile = "deny.txt"

userURL = input("Enter a URL to access: ")

with open (approveFile, "r") as file:
    approveContents = file.read()

with open (denyFile, "r") as file:
    denyContents = file.read()

print()

if userURL in approveContents:
    print("ACCESS GRANTED")
    print("--------------------------------------------------")
    print(f'       CONTENT FROM: {userURL}')
    print("--------------------------------------------------")
    print("This website has been verified as safe by your organization.")
    print("Feel free to browse this content for business or educational purposes.")
    print("Remember to follow the organization's acceptable use policy.")
    print("--------------------------------------------------\n")
    print("This access attempt has been logged to log.txt")
    with open("log.txt", "a") as file:
        file.write(f'Approved {userURL}\n')

elif userURL in denyContents:
    print("ACCESS DENIED")
    print("--------------------------------------------------")
    print(f'       BLOCKED URL: {userURL}')
    print("--------------------------------------------------")
    print("This website has been blocked by your organization's web filter.")
    print("Reason: This URL is on the deny list.")
    print("If you believe this is an error, please contact IT support.")
    print("--------------------------------------------------\n")
    print("This access attempt has been logged to log.txt")
    with open("log.txt", "a") as file:
        file.write(f'Denied {userURL}\n')

else:
    print("URL UNDER REVIEW")
    print("--------------------------------------------------")
    print(f'       PENDING REVIEW: {userURL}')
    print("--------------------------------------------------")
    print("This website is not on the approve or deny lists.")
    print("It has been submitted for review by the security team.")
    print("Access is currently restricted until review is complete.")
    print("Please check back later or contact IT if urgent access is needed.")
    print("--------------------------------------------------\n")
    print("URL has been added to review.txt for security team review.\n")
    print("This access attempt has been logged to log.txt")
    with open("log.txt", "a") as file:
        file.write(f'Review {userURL}\n')


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a URL to access: www.flcc.edu

ACCESS GRANTED
--------------------------------------------------
       CONTENT FROM: www.flcc.edu
--------------------------------------------------
This website has been verified as safe by your organization.
Feel free to browse this content for business or educational purposes.
Remember to follow the organization's acceptable use policy.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.phishingdemo.org

ACCESS DENIED
--------------------------------------------------
       BLOCKED URL: www.phishingdemo.org
--------------------------------------------------
This website has been blocked by your organization's web filter.
Reason: This URL is on the deny list.
If you believe this is an error, please contact IT support.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.opencompsci.com

URL UNDER REVIEW
--------------------------------------------------
       PENDING REVIEW: www.opencompsci.com
--------------------------------------------------
This website is not on the approve or deny lists.
It has been submitted for review by the security team.
Access is currently restricted until review is complete.
Please check back later or contact IT if urgent access is needed.
--------------------------------------------------

URL has been added to review.txt for security team review.

This access attempt has been logged to log.txt
'''

