from turtle import Turtle,Screen

SNAKE_LIST=[]
SNAKE_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.create_snake()
        self.snake_head=SNAKE_LIST[0]
    
    def create_snake(self):
        for i in SNAKE_POSITION:
            new_snake=Turtle("circle")
            new_snake.penup()
            new_snake.color("white")
            new_snake.setposition(i)
            SNAKE_LIST.append(new_snake)
    def add_snake(self):
        new_snake=Turtle("circle")
        new_snake.penup()
        new_snake.color("white")
        new_snake.setposition(SNAKE_LIST[-1].position())
        SNAKE_LIST.append(new_snake)

    def move(self):
        #......................... start end steps
        for i in range(len(SNAKE_LIST)-1, 0, -1):
            previous_snake_x=SNAKE_LIST[i-1].xcor()
            previous_snake_y=SNAKE_LIST[i-1].ycor()
            current_snake=SNAKE_LIST[i]
            current_snake.goto(previous_snake_x,previous_snake_y)
        self.snake_head.fd(MOVE_DISTANCE)
    
    def reset_snake(self):
        global SNAKE_LIST
        for i in SNAKE_LIST:
            i.goto(1000,1000)   # we will send the snake far off the screen so it doesn't stay on the screen
        SNAKE_LIST.clear()
        self.create_snake()
        self.snake_head=SNAKE_LIST[0]
        
    def upMove(self):
        if not self.snake_head.heading()==270:
            self.snake_head.setheading(90)
    def downMove(self):
        if not self.snake_head.heading()==90:
            self.snake_head.setheading(270)
    def leftMove(self):
        if not self.snake_head.heading()==0:
            self.snake_head.setheading(180)
    def rightMove(self):
        if not self.snake_head.heading()==180:    
            self.snake_head.setheading(0)
