# FILE NAME - port_knocking.py

# NAME: Oliver Doty
# DATE: 3/25/2025
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
print("===== PORT KNOCKING FIREWALL SIMULATOR =====")
print("This firewall requires a specific sequence of port connections.")
print("You have 3 attempts to find the correct sequence.")
print("(Hint: Enter port as integers, one at a time)")
attempts = 3
correct_sequence = [2222, 3333, 4444, 5555]

for attempt in range(1, attempts+1):
    print()
    print(f'Attempt {attempt} of 3:')
    
    user_sequence = []
    print("Enter your port knock seqeunce. Enter 0 when finished.")
    for j in range(5):
        user_port = input("Enter port number: ")
        if user_port == "0":
            break
        user_sequence.append(int(user_port))

    if len(user_sequence) != len(correct_sequence):
        print("\nFIREWALL RESPONSE: Connection rejected!")
        print(f'Your sequence had {len(user_sequence)} knocks, but the firewall expects {len(correct_sequence)}.')
    
    elif user_sequence == correct_sequence:
        print("\nFIREWALL RESPONSE: Connection accepted!")
        print("Correct port knocking sequence detected.")
        print("Firewall has opened port 22 for your connection")
        break







########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 3
Enter port number: 4
Enter port number: 5
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 3 knocks, but the firewall expects 4.

Attempt 2 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2222
Enter port number: 3333
Enter port number: 4444
Enter port number: 5555
Enter port number: 0

FIREWALL RESPONSE: Connection accepted!
Correct port knocking sequence detected.
Firewall has opened port 22 for your connection.
'''

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2222
Enter port number: 3333
Enter port number: 4444
Enter port number: 5555
Enter port number: 0

FIREWALL RESPONSE: Connection accepted!
Correct port knocking sequence detected.
Firewall has opened port 22 for your connection.
'''

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 1
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 1 knocks, but the firewall expects 4.

Attempt 2 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2
Enter port number: 3
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 2 knocks, but the firewall expects 4.

Attempt 3 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 4
Enter port number: 5
Enter port number: 6
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 3 knocks, but the firewall expects 4.

MAXIMUM ATTEMPTS REACHED
Firewall has blocked your IP address for 30 minutes.
The correct sequence was: [2222, 3333, 4444, 5555]
'''
