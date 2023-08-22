from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choose = input(f"What do you like? {options}: ").lower()
    while choose not in ("off", "report", "latte", "espresso", "cappuccino"):
        choose = input(f"What do you like? {options}: ").lower()
    if choose == "off":
        print("Shutting down...")
        is_on = False
    elif choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)