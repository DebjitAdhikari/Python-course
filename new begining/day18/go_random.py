from turtle import Turtle,Screen
from random import random
my_turtle=Turtle()
my_turtle.shape("turtle")
my_turtle.color("hotpink")
for _ in range(100):
    angle=(random()*360)
    steps=(random()*100)
    my_turtle.right(angle)
    my_turtle.fd(steps)


sc=Screen()
sc.exitonclick()