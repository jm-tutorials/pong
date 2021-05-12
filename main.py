
from turtle import Screen
import time

from paddle import Paddle
from ball import Ball

screen_width = 800
screen_height = 600
game_is_on = True

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")

rPaddle = Paddle(350)
lPaddle = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(rPaddle.up,"Up")
screen.onkey(rPaddle.down,"Down")
screen.onkey(lPaddle.up,"w")
screen.onkey(lPaddle.down,"s")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()


screen.exitonclick()