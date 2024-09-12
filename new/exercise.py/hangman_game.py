import random
import hangman_art  #from hangman_art import logo
import hangman_words  
print(hangman_art.logo) #print(logo)
word=random.choice(hangman_words.word_list)
print(f"Welcome to Hangman game. Psst, the word is {word}")
blank=[]
for i in word:
    blank+="_"
live=6
end_of_game=False
while not end_of_game:
    letter=input("Enter a letter ").lower()
    if letter in blank:
       print("You have already entered the letter")
    for j in range(len(word)):
        if word[j]==letter:
         blank[j]=letter
    if letter in word:
       print(hangman_art.stages[live])
    elif letter not in word:
       live-=1
       print("Wrong guess, you lose a life")
       print(hangman_art.stages[live])
    print(f"{' '.join(blank)}")
    if "_"not in blank:
       end_of_game=True
       print("Game Won")
    elif live==0:
       print("You Lost")
       end_of_game=True
    
