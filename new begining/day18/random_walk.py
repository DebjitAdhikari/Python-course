from turtle import Turtle,Screen
import random
import turtle
t=Turtle()
t.shape("turtle")
turtle.colormode(255)
# t.color("hotpink")
t.hideturtle()
angle=[0,90,180,270]
t.width(10)
t.speed("fastest")


for i in range(1000):
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.setheading(random.choice(angle))
    t.forward(30)
sc=Screen()
sc.exitonclick()