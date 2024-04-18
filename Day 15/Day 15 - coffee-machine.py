menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def process_coins():
    print("Insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_successful(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def make_coffee(drink, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {drink} ☕️. Enjoy!")


is_on = True
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in ("off", "report", "espresso", "latte", "cappuccino"):
        choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


