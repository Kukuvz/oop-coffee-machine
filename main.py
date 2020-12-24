from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingridients = cofee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingridients and is_payment_successful:
            cofee_maker.make_coffee(drink)