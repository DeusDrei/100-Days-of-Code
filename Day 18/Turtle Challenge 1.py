from turtle import Turtle, Screen

alain = Turtle()
alain.shape("turtle")
alain.color("green")

def square_left():
    for i in range(4):
        alain.forward(300)
        alain.left(90)

def square_right():
    for i in range(4):
        alain.forward(300)
        alain.right(90)

square_left()
alain.left(180)
square_right()
alain.left(90)
square_right()
square_left()

screen = Screen()
screen.exitonclick()
