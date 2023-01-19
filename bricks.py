from turtle import Turtle
import random

colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown']

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

class Brick(Turtle):
    global weights, colors
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(1.5, 3)
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(weights)
    # Borders of the Brick
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15

class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for a in range(-570, 570, 63):
            brick = Brick(a, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for b in range(self.y_start, self.y_end, 32):
            self.create_lane(b)
