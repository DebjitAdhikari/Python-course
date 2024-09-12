from turtle import Screen
from snake import Snake, SNAKE_LIST
import time
from food import Food
from score import Score
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("darkblue") 
s.tracer(0) #stops the animation of the turtle 

game_end=False
t=Snake()
food=Food()
score=Score()
s.listen()
s.onkey(t.upMove,"Up")
s.onkey(t.downMove,"Down")
s.onkey(t.leftMove,"Left")
s.onkey(t.rightMove,"Right")

while not game_end:
    s.update()
    time.sleep(0.1)
    t.move()
    #collison with food
    if t.snake_head.distance(food)<15:
        food.newFood()
        score.increase()
        t.add_snake()
    #collison with wall
    if t.snake_head.xcor()>280 or t.snake_head.xcor()<-280 or t.snake_head.ycor()>280 or t.snake_head.ycor()<-280:
        # game_end=True
        # score.game_over()
        score.game_reset()
        t.reset_snake()
    #collison with tail
    for i in SNAKE_LIST[1:]:
        if i.distance(t.snake_head)<10:
            # game_end=True
            # score.game_over()
            score.game_reset()
            t.reset_snake()
            
            











s.exitonclick()