from replit import clear
from art import logo

print(logo)
bid = {}


def winner():
    amount = 0
    highest = ""
    for key, value in bid.items():
        if value > amount:
            amount = value
            highest = key
    print(f"The Winner is {highest} with a bid of ${amount}!")


while True:
    name = input("What is your name? ")
    money = int(input("How much will you bid? $"))

    bid[name] = money

    ask = input("Are there other users who will bid? (Y/N) ").lower()
    while ask not in ("y", "n"):
        ask = input("Choose only between Y and N: ").lower()
    if ask == "y":
        clear()
    elif ask == "n":
        winner()
        break

