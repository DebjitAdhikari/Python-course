bidding={}
def find_winner(bidding):
    highest_amount=0
    for i in bidding:
        bidding_amount=bidding[i]
        if bidding_amount>highest_amount:
            highest_amount=bidding_amount
            winner=i
    print(f"The winner is {winner}, bid amount ${highest_amount}")
everyone_has_done=False
while everyone_has_done!=True:
    name=input("Enter your name:- ")
    bid=int(input("Enter your bid amount:- $"))
    person=input("Anyone else want to bid ? (Yes/No):- ").lower()
    bidding[name]=bid
    if person=="no":
        find_winner(bidding)
        everyone_has_done=True