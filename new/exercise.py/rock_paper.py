rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("0 for 'Rock', 1 for 'Paper', 2 for 'Scissors' ")
your_choice=int(input("Enter your move "))
bot_choice=random.randint(0,2)
if your_choice==0 and bot_choice==0:
  print(f"Your move -\n{rock}\nComputer's move-\n{rock}\nGame draw.")
elif your_choice==0 and bot_choice==1:
  print(f"Your move -\n{rock}\nComputer's move-\n{paper}\nYou lost.")
elif your_choice==0 and bot_choice==2:
  print(f"Your move -\n{rock}\nComputer's move-\n{scissors}\nYou won.")
#-----------------------------------------------
elif your_choice==1 and bot_choice==0:
  print(f"Your move -\n{paper}\nComputer's move-\n{rock}\nYou won.")
elif your_choice==1 and bot_choice==1:
  print(f"Your move -\n{paper}\nComputer's move-\n{paper}\nGame draw.")
elif your_choice==1 and bot_choice==2:
  print(f"Your move -\n{paper}\nComputer's move-\n{scissors}\nYou lost.")
#----------------------------------------------------
elif your_choice==2 and bot_choice==0:
  print(f"Your move -\n{scissors}\nComputer's move-\n{rock}\nYou lost.")
elif your_choice==2 and bot_choice==1:
  print(f"Your move -\n{scissors}\nComputer's move-\n{paper}\nYou won.")
elif your_choice==2 and bot_choice==2:
  print(f"Your move -\n{scissors}\nComputer's move-\n{scissors}\nGame draw.")

