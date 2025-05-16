# FILE NAME - anything_goes.py

# NAME - Oliver Doty
# DATE - 5/10/2025
# DESCRIPTION - This code with import an AI chatbot




import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great language for beginners and experts alike.",
    "Typing speed tests can improve your accuracy and speed.",
    "Never stop learnign because life never stops teaching.",
    "In a world full of trends, remain a classic."
]

text = random.choice(sentences)
print("----- Typing Speed Test -----")
print("Type the following sentence as fast as you can:\n")
print(f"» {text}")
input("Press Enter when you're ready...")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")

start = time.time()
typed = input("\nStart typing:\n")
end = time.time()

elapsed = end - start
words = len(text.split())
wpm = (len(typed.split()) / elapsed) * 60

# Accuracy calculation
correct = sum(1 for a, b in zip(text, typed) if a == b)
accuracy = (correct / len(text)) * 100

print(f"\n⏱️ Time Taken: {elapsed:.2f} seconds")
print(f"💨 Speed: {wpm:.2f} words per minute")
print(f"🎯 Accuracy: {accuracy:.2f}%")










########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Write a 2-3 paragraph reflection of how things went relying on AI. You can address
   things that went right, things that went wrong (and how you fixed them), ways you
   refined your prompt, things that went wrong and you couldn't fix, how much actual
   Python you had to use.

Overall I found it fairly hard to find something that would work with python. Many ideas pushed more towards
imports and those imports wouldn't work. So I did a bit of browsing. The only part that went "wrong" was I didn't 
like that it was limited to one sentence. So I went through what AI could do. After finding the right
one I didn't entirely like how it was strictly 1 sentence. so I added some extra generated sentences to mix it up.

On the total output of the test. It felt really bland and started really fast so i could see that being a problem.
I wanted to create a timer and use print statements and time.sleep(1). After fixing everything that I felt looked
off about the code. It seems like to works really well. It is simple and easy, looks good and runs well.






'''
