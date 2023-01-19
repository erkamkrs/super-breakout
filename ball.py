from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_distance = MOVE_DISTANCE
        self.y_move_distance = MOVE_DISTANCE
        self.speed(3)
        self.reset()

    def move(self):
        new_y = self.ycor() + self.y_move_distance
        new_x = self.xcor() + self.x_move_distance
        self.goto(x=new_x,y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_distance *= -1

        if y_bounce:
            self.y_move_distance *= -1

    def reset(self):
        self.goto(0, -240)
        self.y_move_distance = 10