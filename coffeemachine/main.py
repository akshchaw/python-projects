from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def report(coffee_maker, money_machine):
    coffee_maker.report()
    money_machine.report()


machine_power = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while machine_power:
    user_choice = input(f"What would you like?({menu.get_items()}): ")
    if user_choice == 'report':
        report(coffee_maker, money_machine)
    elif user_choice == "off":
        print('Powering down. Goodbye!')
        machine_power = False
    else:
        menu_item = menu.find_drink(user_choice)
        if menu_item is not None and coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)