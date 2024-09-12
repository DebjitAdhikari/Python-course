bidders={}
over=False
def max_bid(allbid):
    winner=""
    value=0
    for i in allbid:
        if allbid[i]>value:
            winner=i
            value=allbid[i]
    print(f"The winner is {winner} value:${value}")

while not over:
    name=input("Enter your name: ")
    value=int(input("Enter the bid amount $"))
    bidders[name]=value
    ans=input("Anyone else wanna bid? 'y' or 'n': ")
    if ans=="n":
        over=True
        max_bid(bidders)
