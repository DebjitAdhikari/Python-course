from turtle import Turtle,Screen
import snake
s=Screen()
class Score(Turtle):
    def __init__(self):
        self.current_score=0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} | High Score: {self.high_score}",False,align="center",font=("Courier", 15, "normal"))

    def increase(self):
        self.current_score+=1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",False,align="center",font=("Courier", 24, "normal"))
    def game_reset(self):
        if self.high_score<self.current_score:
            self.high_score=self.current_score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.current_score}")
        self.current_score=0
        self.update_score()