from turtle import Turtle
INITIAL_SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.setheading(20)
        self.steps= INITIAL_SPEED
        
    def move(self):
        self.forward(self.steps)

    def bounce_paddle(self):
        if 0<=self.heading() <= 180:
            new_heading = 180 - self.heading()
        elif 180<self.heading()<=360:
            new_heading = 540 - self.heading()
        self.setheading(new_heading)
        self.steps += 10
        self.move()
        
    def bounce_boundry(self):
        new_heading = (-1) * self.heading()
        self.setheading(new_heading)
        self.move()
        
    def reset_position(self):
        self.goto(0, 0)
        self.setheading(180 - self.heading())
        self.steps = INITIAL_SPEED
        self.move()