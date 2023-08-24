from turtle import Turtle, Screen, colormode
import random

alain = Turtle()
alain.speed(10)
alain.pensize(5)


colormode(255)

for i in range(200):
    alain.color(random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
                )
    alain.forward(20)
    y = [0, 90, 180, 270]
    alain.left(random.choice(y))
    


screen = Screen()
screen.exitonclick()