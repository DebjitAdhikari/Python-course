from turtle import Turtle,Screen
from random import random
my_turtle=Turtle()
my_turtle.shape("turtle")
# my_turtle.color("hotpink")

def shapes(count):
    my_turtle.color(random(),random(),random())
    for _ in range(count):
        my_turtle.forward(100)
        my_turtle.right(360/count)

for i in range(3,10):
    shapes(i)

sc=Screen()
sc.exitonclick()