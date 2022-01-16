
from turtle import Turtle, Screen
INITIAL_PADDLE_LENGTH = 3
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(((-1)**player) * 350,0 )

    def up(self):
        new_ycor = self.ycor()+20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)