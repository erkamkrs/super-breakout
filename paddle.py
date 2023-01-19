from turtle import Turtle
import random

MOVE_DISTANCE = 80

# Creating a Paddle
class Paddle(Turtle):
    colors = ['green','orange','yellow','pink','purple','gold','gray','brown',]
    def __init__(self):
        super().__init__()
        self.color(random.choice(self.colors))
        self.shape("square")
        self.speed(8)
        self.penup()
        self.shapesize(1, 10)
        self.goto(0, -280)


    def move_right(self):
        self.forward(MOVE_DISTANCE)


    def move_left(self):
        self.backward(MOVE_DISTANCE)


