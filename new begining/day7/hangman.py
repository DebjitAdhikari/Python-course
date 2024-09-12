import random
# 1st way............
# import anything
# print(anything.greet)

# 2nd way...........
from anything import greet
print(greet)

words=["avocado","superman","debjit"]
guess = random.choice(words)
print(guess)

# display=["_" for i in range(len(guess))] #using list comprehension
display=[]
for i in range(len(guess)):
    display+="_"
live=5
over=False
allblank=True

while not over:
    print(display)
    print(f"You have {live} left")
    letter=input("Enter a letter: ")
    if letter in guess:
        for i in  range(len(guess)):
            if guess[i]==letter:
                display[i]=letter
    else:
        live-=1
    if not "_" in display:
        print("you won")
        over=True
    if live==0:
        print("you lost")
        over=True
print(f"Final answer: {display}")

    