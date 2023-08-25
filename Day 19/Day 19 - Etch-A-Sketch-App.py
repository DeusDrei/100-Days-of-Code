from turtle import Turtle, Screen

alain = Turtle()
screen = Screen()

def move_forward():
    alain.forward(10)

def turn_left():
    alain.left(10)

def move_backwards():
    alain.backward(10)

def turn_right():
    alain.right(10)

def screen_clear():
    alain.clear()
    alain.penup() 
    alain.home()
    alain.pendown()

def dont_draw():
    alain.penup()

def ok_draw():
    alain.pendown()

screen.listen()
screen.onkeypress(fun=move_forward,key="w")
screen.onkeypress(fun=turn_left,key="a")
screen.onkeypress(fun=move_backwards,key="s")
screen.onkeypress(fun=turn_right,key="d")
screen.onkeypress(fun=screen_clear,key="c")
screen.onkeypress(fun=dont_draw,key="q")
screen.onkeypress(fun=ok_draw,key="e")

screen.exitonclick()