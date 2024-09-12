from high_low_art import logo
from high_low_art import vs
from high_low_data import data
import random
print(logo)
person_a=random.choice(data)
point=0
end_of_game=False
while not end_of_game:
    person_b=random.choice(data)
    print(f"Compare A: {person_a['name']} a {person_a['description']} from {person_a['country']}")
    print(vs)
    print(f"Compare B: {person_b['name']} a {person_b['description']} from {person_b['country']}")
    ans=input("Who has more followers ? Type 'A' or 'B':-").lower()
    if ans=="a":
        if person_a["follower_count"]>person_b["follower_count"]:
            point+=1
            print("Correct guess.")
            print(f"Current score is {point}")
        else:
            print("Wrong answer")
            print(f"Final score {point}")
            break
    else:
        if person_a["follower_count"]<person_b["follower_count"]:
            point+=1
            print("Correct guess.")
            print(f"Current score is {point}")
        else:
            print("Wrong answer")
            print(f"Final score {point}")
            break
    person_a=person_b
