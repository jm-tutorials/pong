
from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen_width = 800
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")

rPaddle = Paddle(350)
lPaddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rPaddle.up,"Up")
screen.onkey(rPaddle.down,"Down")
screen.onkey(lPaddle.up,"w")
screen.onkey(lPaddle.down,"s")

while scoreboard.game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top/bottom wall
    if abs(ball.ycor()) > 281:
        ball.bounce_y() 
        ball.move()

    # Detect collision with left and right paddle
    if (ball.distance(rPaddle) < 50 and ball.xcor() > 320) or (ball.distance(lPaddle) < 50 and ball.xcor() < -320):
        ball.bounce_x() 
        ball.move()

    # Detect collision with right wall, score 
    if ball.xcor() > 380:
        scoreboard.addPoint(left_player=True)
        ball.reset_position()

    # Detect collision with left wall, score 
    elif ball.xcor() < -380:
        scoreboard.addPoint(left_player=False)
        ball.reset_position()

screen.exitonclick()