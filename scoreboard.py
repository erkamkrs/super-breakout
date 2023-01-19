from turtle import Turtle
FONT = ("Helvetica", 15)

try:
    score = int(open('high_score.txt', 'r').read())
except FileNotFoundError:
    score = open('high_score.txt', 'w').write(str(0))
except ValueError:
    score = 0


class Scoreboard(Turtle):
    def __init__(self, user_lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-570, y=260)
        self.lives = user_lives
        self.highScore = score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highScore} \n"
                   f"Lives: {self.lives}", align="left", font=FONT)


    def add_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.update_score()


    def reset_scoreboard(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("high_score.txt", "w").write(str(self.highScore))


