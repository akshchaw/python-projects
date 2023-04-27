from turtle import Turtle

FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-25, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(-25, 0)
        self.write("game over", font=FONT)

    def add(self):
        self.score += 1
        self.update_scoreboard()
