from turtle import Turtle

WIDTH = 1
HEIGHT = 1
BASE_MOVE_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.coordinates = self.position()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BASE_MOVE_SPEED

    def move(self, h=1, v=1):
        past_x, past_y = self.position()
        new_x = past_x + self.x_move
        new_y = past_y + self.y_move
        self.goto((new_x,new_y))

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto((0,0))
        self.showturtle()
        self.move_speed = BASE_MOVE_SPEED
        self.bounce_x()
