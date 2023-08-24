import turtle as t
import random

alain = t.Turtle()
t.colormode(255)
alain.speed("fastest")
alain.penup()
alain.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
alain.setheading(225)
alain.forward(300)
alain.setheading(0)

for dot_count in range(1, 101):
    alain.dot(20, random.choice(color_list))
    alain.forward(50)

    if dot_count % 10 == 0:
        alain.setheading(90)
        alain.forward(50)
        alain.setheading(180)
        alain.forward(500)
        alain.setheading(0)


screen = t.Screen()
screen.exitonclick()