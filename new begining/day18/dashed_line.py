from turtle import Turtle,Screen

my_turtle=Turtle()
my_turtle.shape("turtle")
my_turtle.color("hotpink")
dash=5
gap=5

for _ in range(50):
    my_turtle.forward(dash)
    my_turtle.penup()
    my_turtle.forward(gap)
    my_turtle.pendown()

sc=Screen()
sc.exitonclick()