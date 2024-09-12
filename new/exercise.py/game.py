print('''Welcome! to Treasure Hunting   
----------------------------------
Hey, you are in dangerous island. Only way to win this game is to find the treasure as
soon as possible.
Attention, your game is going to start........
*****
loading...
let's begin...
''')
print("This island is deserted. You spawn into a dark room. ")
flag=0
control=input("Where do you want to go ? (Right / Left) ")
control=control.lower()
if control=="right":
    print("Congrats! You have seen a boat. It's a hope to find the treasure")
    control1=input("You will 'Swim' or 'Wait' ? ")
    control1=control1.lower()
    if control1=="swim":
        print("There is shark in the ocean, what you will do now ?")
        control2=input("'Swim' or 'Wait' ? ")
        control2=control2.lower()
        if control2=="wait":
            print("Wow, you are smart. You have made the right decision.")
            flag=1
        elif control2=="swim":
            print("Game over.")
            print("You are spotted by the shark.\nTry again.")
            exit

    elif control1=="wait":
        print("There is two ship, Red flag ship and White flag ship.")
        control3=input("Which of the ship do you want to choose ? ")
        control3=control3.lower()
        if control3=="white":
            print("Indeed, you have choosen a good ship...")
            flag=1
        else:
            print("Game over.\nThat was a pirate ship. You are beheaded by the pirates now\nTry again.")
            exit
    if flag==1:
        print("\nYou arrived in a treasure island now. Just few more carefull steps and Victory\n")
        print("After 2 hours...\n")
        print("You arrived here in front of a room. It has three doors. You have only one key.")
        control4=input("Which door do you want to open ? [Red/Green/Yellow] ")
        control4=control4.lower()
        if control4=="yellow":
            print("Congo!!! You have found the treasure.\nYou won the game.")
        elif control4=="red":
            print("Game over.\nIt was a fire room. You have burnt into ashes.\nTry again.")
        else:
            print("Game over.\nWrong door. This room is full of snakes.\nTry again.")
else:
    print("Game over. You are dead, you fall into hole")