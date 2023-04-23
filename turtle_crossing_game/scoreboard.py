from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-270, 270)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level:{self.level}", font=FONT)

    def reset(self):
        self.goto(-70, 0)
        self.write(f"Game Over", font=FONT)

    def increase(self):
        self.level += 1
        self.display()
