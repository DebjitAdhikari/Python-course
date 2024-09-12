from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.write_again()
    def write_again(self):
        self.clear()
        #left
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        #right
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
