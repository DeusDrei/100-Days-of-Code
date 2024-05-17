import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
gray = 0
black = 0
red = 0

for i in color:
    if i == "Gray":
        gray += 1
    elif i == "Black":
        black += 1
    elif i == "Cinnamon":
        red += 1

data_dict = {
    "Fur color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
