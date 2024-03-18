import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:    
    answer = screen.textinput(title=f"Guessed states {len(guessed)}/50", prompt="Enter a state: ").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed.append(answer)
        alain = turtle.Turtle()
        alain.hideturtle()
        alain.penup()
        state_data = data[data.state == answer]
        alain.goto(x=int(state_data.x), y=int(state_data.y))
        alain.write(answer)

