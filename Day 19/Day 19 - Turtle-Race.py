from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make a bet", prompt="Pick a color (red, orange, green, black, blue, violet, brown): ")

t_color = ["red", "orange", "green", "black", "blue", "violet", "brown"]
y_position = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []

is_on = False

if bet:
    is_on = True

while is_on:

    for i in all_turtles:
        if i.xcor() > 230:
            is_on = False
            winner = i.pencolor()
            if winner == bet:
                print(f"You Win! {winner} is the winning turtle!")
            else:
                print(f"You lose. {winner} is the winning turtle.")

        distance = random.randint(0, 10)
        i.forward(distance)


screen.exitonclick()
