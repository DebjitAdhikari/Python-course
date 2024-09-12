from turtle import Turtle
LEVEL_FONT = ("Courier", 14, "normal")
GAME_OVER_FONT=("Courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.update_score()
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_score()
    def update_score(self):
        self.write(f"Level: {self.score}",align="center",font=LEVEL_FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=GAME_OVER_FONT)
