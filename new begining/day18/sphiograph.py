from turtle import Turtle,Screen
import random
import turtle

t=Turtle()
# t.shape("turtle")
turtle.colormode(255)
# t.color("hotpink")
t.speed(10)
def spirograph(gaph_size):
    for i in range(int(360/gaph_size)):
        t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        t.circle(100)
        t.setheading(t.heading()+gaph_size)
spirograph(5)
sc=Screen()
sc.exitonclick()