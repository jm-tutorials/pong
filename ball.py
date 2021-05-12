from turtle import Turtle

WIDTH = 1
HEIGHT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(45)
    
    def move(self):
        
