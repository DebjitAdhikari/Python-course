from turtle import Turtle,Screen
t=Turtle()
s=Screen()
s.listen()
def move():
    t.fd(10)

s.onkey(key="space",fun=move)


s.exitonclick()