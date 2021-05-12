from turtle import Turtle

WIDTH = 1
HEIGHT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.coordinates = self.position()
        self.x_direction = 1
        self.y_direction = 1
    
    def setXDirection(self,h):
        self.x_direction = h 

    def setYDirection(self,v):
        self.y_direction = v 

    def move(self, h=1, v=1):
        past_x, past_y = self.position()
        new_x = past_x + (10 * self.x_direction)
        new_y = past_y + (10 * self.y_direction)
        self.goto((new_x,new_y))