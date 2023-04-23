import colorgram
import turtle
import random

# colors = colorgram.extract('image.jpeg', 12)
# colors_rgb = []
# for i in colors:
#     colors_rgb.append((i.rgb.r,i.rgb.g,i.rgb.b))
# print(colors_rgb)

colors_rgb =[(235, 36, 110), (238, 73, 35), (144, 28, 66), (8, 147, 93), (229, 168, 43), (183, 159, 47), (46, 191, 231), (29, 126, 194)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.setx(-300)
tim.sety(-300)

def dot_line():
    for _ in range(10):
        tim.dot(20,random.choice(colors_rgb))
        tim.forward(50)

for i in range(10):
    tim.setx(-300)
    num = 50*i -300
    tim.sety(num)
    dot_line()



screen = turtle.Screen()
screen.exitonclick()
