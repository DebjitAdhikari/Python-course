import random
NUMBER=random.randint(1,101)

def easy_level():
    live=10
    while live!=0:
        print(f"You have {live} left, guess the number correctly.")
        guess=int(input("Enter the nubmer:- "))
        if guess==NUMBER:
            print("Correct. You won")
            break
        elif guess<NUMBER:
            print("Too Low.")
            live-=1
        elif guess>NUMBER:
            print("Too High.")
            live-=1
    if live==0:
        print("You lose.")
    else:
        print("You won.")    
def hard_level():
    live=5
    while live!=0:
        print(f"You have {live} left, guess the number correctly.")
        guess=int(input("Enter the nubmer:- "))
        if guess==NUMBER:
            print("Correct. You won")
            break
        elif guess<NUMBER:
            print("Too Low.")
            live-=1
        elif guess>NUMBER:
            print("Too High.")
            live-=1
    if live==0:
        print("You lose.")
    else:
        print("You won.")

print("Guess the number between 1 to 100.")
level=input("Choose the difficulty 'easy' and 'hard':- ").lower()
if level=="easy":
    easy_level()
else:
    hard_level()
