from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title='Enter your bet',prompt='Which turtle will win the race')
colors = ['red','orange','yellow','green','blue','purple']
all_turtles = []

tim = Turtle()
tim.penup()
tim.goto(210,-100)
tim.pendown()
tim.setheading(90)
 
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=-90+i*30)
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f'You have won, {winning_color} has won the race')
            else:
                print(f'You have lost, {winning_color} has won the race')
            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()