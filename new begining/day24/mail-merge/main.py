#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./input/Names/invited_names.txt") as file:
    all_names=file.read().split("\n")

with open("./input/Letters/starting_letter.txt") as file:
    the_letter=file.read()
    for i in all_names:
        with open(f"./output/ReadyToSend/letter_for_{i}.txt",mode="w") as file:
            new_letter=the_letter.replace("[name]",i)
            file.write(new_letter)
     
# with open("./")
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp