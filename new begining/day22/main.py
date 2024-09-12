from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score
s=Screen()
s.bgcolor("darkblue")
s.setup(width=800,height=600)
s.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
s.listen()

s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")

s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")

ball=Ball()
# ball.move()
score=Score()

game_end=False
while not game_end:
    time.sleep(ball.ball_speed)
    s.update()
    ball.move()
    # collides with the top and down
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #collides with the paddles
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #right player misses the ball
    if ball.xcor()>390:
        ball.ball_miss()
        score.l_score+=1
        score.write_again()
    #left player misses the ball
    if ball.xcor()<-390:
        ball.ball_miss()
        score.r_score+=1
        score.write_again()
        
s.exitonclick()