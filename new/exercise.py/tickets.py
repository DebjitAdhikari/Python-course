height=int(input("Enter your height in cm "))
if height>120:
    print("Yes, you are eligible for ride")
    age=int(input("Enter your age "))
    bill=0
    if age<12:
        bill=5
        print("Child tickets are $5")
    elif age>=12 and age<=18:
        bill=7
        print("Youth tickets are $7")
    elif age>18 and age<45:
        bill=12
        print("Adult tickets are $12")
    elif age>=45 and age<=55:
        print("You are allowed to ride free")
    wants_photo=input("Do you wanna click photo for $3 ? (Y/N) ")
    if wants_photo=="Y" or wants_photo=="y":
        bill+=3
    print(f"Your final bill amount is {bill}$")
else:
    print("No, you are not allowed to ride")