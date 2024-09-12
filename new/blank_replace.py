import random
my_word=["Kakarot","Levi","Eren","Elephant"]
randome=random.choice(my_word)
print("The word is ",randome)
randome=randome.lower()
blank=[]
for i in randome:
    blank+="_"
print(blank)
end_of_game=False
while not end_of_game: #blank.count("_")!=0:
    choose_letter=input("Enter a letter ").lower()

    for j in range(0,len(randome)):
        if choose_letter==randome[j]:
            blank[j]=choose_letter
    print(blank)
    if "_" not in blank:
        end_of_game=True
        print("You won")