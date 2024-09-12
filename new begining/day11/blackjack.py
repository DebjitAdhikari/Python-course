import random
from blackjack_art import logo
print(logo)

#give random cards
def randomCards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#draw 2 cards for each at the game start
def gameStart(who):
    who.append(randomCards())
    who.append(randomCards())

#getting one cards
def getCards(who):
    who.append(randomCards())

#check who scored high
def checkWinner(player,computer):
    if sum(player)>sum(computer):
        print(f"You won the game, your cards:{player} total score:{sum(player)}")
    else:
        print(f"Computer won the game, Computer cards:{computer} total score:{sum(computer)}")

#check if over 21
def isLimitOver(player):
    if sum(player)>21:
        return True
    else:
        return False
    
over=False
end=False
while not end:
    ans=input("Wanna play blackjack 'y' or 'n': ")
    if ans=="n":
        break
    computer=[]
    player=[]
    gameStart(computer)
    gameStart(player)
    while not over:
        print(f"Your cards: {player}, total hand: {sum(player)}")
        print(f"Computer's cards; {computer}, total hand: {sum(computer)}")
        more=input("You wanna draw more cards? 'y' or 'n': ")
        if more=="n":
            checkWinner(player,computer)
            over=True
        else:
            getCards(player)
            getCards(computer)
            limit=isLimitOver(player)
            if limit==True:
                print("You lost you")

                #incomplete i didn't have the time complete this shit game




