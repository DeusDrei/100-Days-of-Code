from turtle import Turtle, Screen

alain = Turtle()

def dashed_line():
    for i in range(15):
        alain.forward(10)
        alain.penup()
        alain.forward(10)
        alain.pendown()

def go_home():
    alain.penup()
    alain.home()
    alain.pendown()

dashed_line()
go_home()
alain.left(180)
dashed_line()
go_home()
alain.right(90)
dashed_line()
go_home()
alain.left(90)
dashed_line()
go_home()


screen = Screen()
screen.exitonclick()