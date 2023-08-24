from turtle import Turtle, Screen, colormode
from random import randint

alain = Turtle()

def gon(sides):
    angle = 360 / sides
    for i in range(sides):
        alain.forward(100)
        alain.right(angle)

colormode(255)

i = 3

while i <= 9:
    alain.color(randint(0, 255),
                randint(0, 255),
                randint(0, 255)
                )
    gon(i) 
    i += 1


screen = Screen()
screen.exitonclick()