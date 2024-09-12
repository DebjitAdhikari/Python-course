from turtle import Turtle,Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_list=[]
race_on=True

s=Screen()
s.bgcolor("black")
s.setup(width=500,height=400)
user_input=s.textinput("Your bet!","Who will win?").lower()

for i in range(len(colors)):
    t=Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230,y=y_positions[i])
    turtle_list.append(t)



while race_on:
    # t=random.choice(turtle_list)
    # t.fd(random.randint(0,10))
    for i in turtle_list:
        if i.xcor()>230:
            if i.pencolor==user_input:
                print("you won")
            else:
                print("you lost")
            race_on=False
            break
        i.fd(random.randint(0,10))

s.exitonclick()
