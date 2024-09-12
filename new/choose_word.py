import random
my_word=["Kakarot","Levi","Eren","Elephant"]
choose_letter=input("Enter a letter ").lower()
randome=random.choice(my_word)
randome=randome.lower()
print("You have choosen ",choose_letter)
for i in range(0,len(randome)):
    if choose_letter==randome[i]:
        print("Right")
    else:
        print("Wrong")