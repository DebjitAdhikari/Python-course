name1=input("Enter your name - ")
name2=input("Enter his/her name - ")
my_name=name1.lower()
her_name=name2.lower()
our_name=my_name+her_name
count_t=our_name.count("t")
count_r=our_name.count("r")
count_u=our_name.count("u")
count_e=our_name.count("e")
l=our_name.count("l")
o=our_name.count("o")
v=our_name.count("v")
e=our_name.count("e")
true=count_t+count_r+count_u+count_e
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"Your love score is - {love_score}%, you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"Your love score is - {love_score}%, you are alright together.")
else:
    print(f"You love score is - {love_score}")