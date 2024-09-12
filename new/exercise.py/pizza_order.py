print("Welcome! to Pizza Deliveries")
print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25")
print("Pepproni for small pizza: +$2\nPepproni for medium & large pizza: +$3\nCheese for any pizza: +$1\n")
size=input("What size of Pizza do you really want ? [S/M/L] ")
want_pep=input("Do you want Pepproni ? [Y/N] ")
want_cheese=input("Do you want extra cheese ? [Y/N] ")
bill=0
if size=="s" or size=="S":
    bill=15
    if want_pep=="Y" or want_pep=="y":
        bill+=2
    if want_cheese=="Y" or want_cheese=="y":
        bill+=1
elif size=="m" or size=="M":
    bill=20
    if want_pep=="Y" or want_pep=="y":
        bill+=3
    if want_cheese=="Y" or want_cheese=="y":
        bill+=1
else:
    bill=25
    if want_pep=="Y" or want_pep=="y":
        bill+=3
    if want_cheese=="Y" or want_cheese=="y":
        bill+=1
print(f"Your total bill is ${bill}")