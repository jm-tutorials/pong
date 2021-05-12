from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self,starting_x):
        super().__init__()
        #self.shape("rectangle")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setx(starting_x)

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def up(self):
        self.setheading(UP)
        self.move()

    def down(self):
        self.setheading(DOWN)
        self.move()

