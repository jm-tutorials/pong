
from turtle import Screen

from paddle import Paddle


screen_width = 800
screen_height = 600
WIDTH = 20
HEIGHT = 100

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
#screen.update()

screen.listen()
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")
screen.update()


screen.exitonclick()