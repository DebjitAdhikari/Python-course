def getname(first,last):
    return f"{first.title()} {last.title()}"
print(getname(input("Your first name: "),input("Your last name: ")))