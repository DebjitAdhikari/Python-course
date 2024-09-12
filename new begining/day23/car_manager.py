from turtle import Turtle
import random
COLORS = ["coral","skyblue","lavender","orange", "yellow", "green", "blue","darkgreen", "gold", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        chance=random.randint(1,6)
        if chance==6:
            new_car=Turtle("square")            
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300,random.randint(-250,250))
            self.car_list.append(new_car)
    def move_cars(self):
        for i in self.car_list:
            i.backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT

