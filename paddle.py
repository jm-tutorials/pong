from turtle import Turtle

WIDTH = 100
LENGTH = 20
STRETCH_WIDTH = WIDTH/20
STRETCH_LENGTH = LENGTH/20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self,starting_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setx(starting_x)

    def up(self):
        current_x,current_y = self.position()
        self.goto((current_x, current_y + MOVE_DISTANCE))

    def down(self):
        current_x,current_y = self.position()
        self.goto((current_x, current_y - MOVE_DISTANCE))

