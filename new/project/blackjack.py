import random
from blackjack_art import logo
computer_choice=[]
my_choice=[]
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def game_score(card_list):
    """Here we are going to calculate the total cards score in the list"""
    if sum(card_list)==21 and len(card_list)==2:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)
def comparison(user,computer):
    if user==0:
        return "BlackJack. You Won."
    elif computer==0:
        return "Opponents have BlackJack. You Lose."
    elif user>21:
        return "You Lose."
    elif computer>21:
        return "You Won."
    elif user>computer:
        return "You Won."
    elif computer>user:
        return "You Lose."
def game():
    print(logo)
    end_of_game=False
    for i in range(2):
        my_choice.append(deal_card())
        computer_choice.append(deal_card())
    while not end_of_game:
        user=game_score(my_choice)
        computer=game_score(computer_choice)
        print(f"Your card {my_choice}. Total score {user}")
        print(f"Computer's card {computer_choice[0]}.")
        if user==0 or computer==0 or user>21:
            end_of_game=True
        else:
            should_deal=input("Type 'y' to get another card 'n' to pass").lower()
            if should_deal=="y":
                my_choice.append(deal_card())
            else:
                end_of_game=True
    while computer!=0 and computer<17:
        computer_choice.append(deal_card())
        computer=game_score(computer_choice)
    print(f"Your cards {my_choice}. Total score:- {user}")
    print(f"Opponent's cards {computer_choice}. Total score:- {computer}")
    print(comparison(user,computer))
while input("Wanna play again buddy ? (Y/N)").lower()=="y":
    game()
