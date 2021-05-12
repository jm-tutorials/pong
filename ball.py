from turtle import Turtle

WIDTH = 1
HEIGHT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
    
    def move(self):
        new_position = map(lambda x: x+10, self.position())
        self.goto(new_position)

