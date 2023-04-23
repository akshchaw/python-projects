MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

power_on = True
input_money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${input_money}")


def check_resources(coffee):
    ingredients = MENU[coffee]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            return False
    return True


def check_money(coffee):
    total_cost = MENU[coffee]['cost']
    quarters = int(input('How many quarters are you entering: '))
    dimes = int(input('How many dimes are you entering: '))
    nickles = int(input('How many nickles are you entering: '))
    pennies = int(input('How many pennies are you entering: '))
    total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    total_change = round(total_money - total_cost, 2)
    if total_money >= total_cost:
        print(f"Here is ${total_change} dollars in change. ")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee):
    total_cost = MENU[coffee]['cost']
    ingredients = MENU[coffee]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f'Here is your {coffee}')
    return total_cost


def coffee_entry(coffee):
    if check_resources(coffee) and check_money(coffee):
        return make_coffee(coffee)
    return None


while power_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'report':
        report()
    elif user_input == 'off':
        print('Powering down. Goodbye!')
        power_on = False
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        add_money = coffee_entry(user_input)
        if add_money is not None:
            input_money += add_money
    else:
        print('Enter a valid entry')
