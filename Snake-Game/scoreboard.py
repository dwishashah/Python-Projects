from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("courier", 22, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.high_score}', align='center',
                   font=('courier', 24, 'normal'))

    def reset_scoreboard(self):
        self.goto(0, 0)
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f'Score: {self.score}, High Score: {self.high_score}', align='center',
                   font=('courier', 24, 'normal'))
