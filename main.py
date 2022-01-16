from turtle import Turtle, Screen
import random
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()
INITIAL_SPEED = 20
WINNING_SCORE = 5

score = Scoreboard()

screen.listen()
screen.onkey(fun=paddle1.up, key='w')
screen.onkey(fun=paddle1.down, key='s')

screen.onkey(fun=paddle2.up, key='Up')
screen.onkey(fun=paddle2.down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # can change this to increase the speed of the ball
    ball.move()

    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.xcor() > 350:
            score.addscore(1)
        else:
            score.addscore(2)
        ball.reset_position()
    if ball.xcor() < 0 and ball.xcor() - paddle1.xcor() < 15 and paddle1.ycor()-50 < ball.ycor() < paddle1.ycor()+50:
        ball.bounce_paddle()
        score.addscore(1)
        score.boardupdate()
    if ball.xcor() > 0 and paddle2.xcor() - ball.xcor()< 15 and paddle2.ycor()-50 < ball.ycor() < paddle2.ycor()+50:
        ball.bounce_paddle()
        score.addscore(2)
        score.boardupdate()
    if (ball.ycor() > 280 or ball.ycor() < -280) and -350 <= ball.xcor() <= 350:
        ball.bounce_boundry()
    if score.l_score == WINNING_SCORE or score.r_score == WINNING_SCORE:
        game_is_on = False
        if score.l_score == WINNING_SCORE:
            score.game_over(1)
        else:
            score.game_over(2)


screen.exitonclick()