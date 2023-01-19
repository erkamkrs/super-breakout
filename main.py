import time
import turtle as tr
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from tkinter import messagebox

screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard(user_lives=3)
bricks = Bricks()
paddle = Paddle()
ball = Ball()
game_is_on = True


screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

def check_wall_collision():
    global ball
# Detect collusion with horizantal walls
    if ball.xcor() < -570 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
# Detect collusion with upper wall
    if ball.ycor() > 280:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
# If failed to hit the ball
    if ball.ycor() < -280:
        ball.reset()
        time.sleep(0.5)
        scoreboard.lives -= 1
        scoreboard.update_score()
        if scoreboard.lives <= 0:
            game_over()
            scoreboard.reset_scoreboard()
        return


def paddle_hit():
    global ball, paddle
    paddle_x= paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
    # When the Paddle is on the right side
        if paddle_x > 0:
            if ball_x > paddle_x:
    # If the ball hits right side of the paddle thus it should go right

                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        elif paddle_x < 0:
    # When the Paddle is on the left side
            if ball_x < paddle_x:
    # If the ball hits left side of the paddle thus it should go left
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

    # When the ball is in the middle
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

def bricks_hit():
    global ball, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 45:
            brick.quantity -= 1
            scoreboard.score += 100
            scoreboard.update_score()
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)



            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

def game_over():
    global game_is_on
    game_is_on = False
    messagebox.showinfo(title="Game Over", message=f"Game is Over. Your score is {scoreboard.score}")



while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    bricks_hit()
    check_wall_collision()
    paddle_hit()


tr.mainloop()


