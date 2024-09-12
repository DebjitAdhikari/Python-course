from turtle import Turtle,Screen
import random
import turtle
import colorgram
t=Turtle()
turtle.colormode(255)
t.speed(10)
t.penup()
t.hideturtle()
#.....to extract the colors...........
# colors=colorgram.extract("./image.jpg",10)
# rgb_colors=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

color_list=[(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239)]

t.setheading(225)
t.forward(300)
t.setheading(0)
for i in range(1, 100+1):
    t.dot(20,random.choice(color_list))
    # t.dot(20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t.forward(50)
    if(i%10==0):
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)
        

sc=Screen()
sc.exitonclick()