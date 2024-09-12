import random
people=input("Enter everyone's name which has to be separated by comma ")
name=people.split(", ")
size=len(name)
luck=random.randint(0,size-1)
print(f"Today {name[luck]} will pay the bill")