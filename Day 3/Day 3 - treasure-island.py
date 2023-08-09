print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


def intro():
    cross = input(
        "You see two paths which way will you go? (left or right) ").lower()
    if cross == "left":
        scenario1()
    else:
        print("You fall into a hole.")
        print("Game Over.")


def scenario1():
    ask = input("There is a lake what will you do? (swim or wait) ").lower()
    if ask == "wait":
        scenario2()
    else:
        print("You were attacked by a trout.")
        print("Game Over.")


def scenario2():
    door = input(
        "While waiting, 3 doors suddenly appeared. Which will you choose? (Red, Yellow, or Blue) "
    ).lower()
    if door == "red":
        print(
            "After entering the red door, the door closed itself. Flames engulf the room and you were burned to death."
        )
        print("Game Over.")
    elif door == "blue":
        print(
            "After entering the blue door, the door closed itself. Tons of wild beasts appeared and you were eaten alive."
        )
        print("Game Over.")
    elif door == "yellow":
        print(
            "As you open the yellow door, you see the treasure chest. The search is over."
        )
        print("You Win!")
    else:
        print("You fell to a spike trap.")
        print("Game Over.")


intro()
