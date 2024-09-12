import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")
t=Player()
screen.listen()
screen.onkey(t.go_up,"Up")
car=CarManager()
score=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #create cars 
    car.create_car()
    car.move_cars()
    #collison with cars
    for i in car.car_list:
        if i.distance(t)<20:
            game_is_on=False
            score.game_over()
            screen.bgcolor("red")
            break
    #detect if reaches the end
    if t.is_endline():
        t.goto_start()
        car.increase_speed()
        score.increase_score()
        


screen.exitonclick()

