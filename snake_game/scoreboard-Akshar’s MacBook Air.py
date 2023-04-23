from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-25,280)
        self.write(f"Score:{self.score}", font=("Verdana", 15, "normal"))

    def reset(self):
        self.score = 0

    def __add__(self):
        self.score+=1
        self.write(f"Score:{self.score}", font=("Verdana", 15, "normal"))
