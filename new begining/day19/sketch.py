from turtle import Turtle,Screen
t=Turtle()
s=Screen()
s.bgcolor("black")
t.color("hotpink")
s.listen()
def forwards():
    t.fd(10)
def backwards():
    t.backward(10)
def antiClockwise():
    
    t.setheading(t.heading()+10)
def clockwise():
    t.setheading(t.heading()-10)
def clearScreen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
s.onkey(key="w",fun=forwards)
s.onkey(key="s",fun=backwards)
s.onkey(key="a",fun=antiClockwise)
s.onkey(key="d",fun=clockwise)
s.onkey(clearScreen,"c")
s.exitonclick()