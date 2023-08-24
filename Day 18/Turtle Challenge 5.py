import turtle as t
import random

alain = t.Turtle()
alain.speed("fastest")
t.colormode(255)


for i in range(72):
    alain.color(random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                )
    alain.circle(100)
    alain.left(5)


screen = t.Screen()
screen.exitonclick()
