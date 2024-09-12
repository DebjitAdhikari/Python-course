import random
from higher_lower_data import data
over=False
def getRandomData():
    return random.choice(data)
def showData(theData):
    print(f"{theData["name"]} a {theData["description"]} from {theData["country"]}")
def getcorrectOpt(a,b):
    if a["follower_count"]>b["follower_count"]:
        return "a"
    else:
        return "b"
    
def getcorrectans(a,b):
    opt=getcorrectOpt(a,b)
    if opt=="a":
        return a
    else:
        return b
    
while not over:
    ans=input("Want to play 'y'or'n': ")
    if ans=="n":
        over=True
    else:
        a_opt=getRandomData()
        b_opt=getRandomData()
        end=False
        score=0
        while not end:
            print(f"Current score: {score}")
            showData(a_opt)
            print("vs")
            showData(b_opt)
            #print(a_opt["follower_count"],b_opt["follower_count"])
            opt=input("Who has the more followers? 'a' or 'b': ")
            correct=getcorrectOpt(a_opt,b_opt)

            if correct != opt:
                print(f"Sorry, wrong answer. You lost the game. Highscore {score}")
                end=True
            else:
                a_opt=getcorrectans(a_opt,b_opt)
                b_opt=getRandomData()
                score+=1

    

   