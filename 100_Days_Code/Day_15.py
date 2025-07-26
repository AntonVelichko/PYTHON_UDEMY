##########################################################################################################################
###  COFFEE MACHINE PROJECT  ###

............................................................................................
../my_solution.py

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
    "water": 250,
    "milk": 200,
    "coffee": 28,
}

total_money = 0


def is_resource_enough(ingredients):
    """Returns True if all required ingredients are available; otherwise prints all missing items and returns False."""
    missing_ingridients = []
    for ingredient, required_amount in ingredients.items():
        available_amount = resources.get(ingredient, 0)
        if available_amount < required_amount:
            missing_ingridients.append(ingredient)

    if missing_ingridients:
        print(f"Sorry there is not enough {', '.join(missing_ingridients)}!")   # Sorry there is not enough water, milk, coffee!
        return False

    return True


def process_coins():
    """Prompts user to input the number of coins and returns the total amount in dollars."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))   # 0.25 each
    dimes = int(input("How many dimes? "))         # 0.10 each
    nickles = int(input("How many nickles? "))     # 0.05 each
    pennies = int(input("How many pennies? "))     # 0.01 each

    total = (
        quarters * 0.25 +
        dimes * 0.10 +
        nickles * 0.05 +
        pennies * 0.01
    )

    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    if money_received - drink_cost >= 0:
        user_change = round(money_received - drink_cost, 2)
        print(f"You've inserted ${money_received}. Your change is ${user_change}")
        global total_money
        total_money += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded - ${money_received}")
        return False


def make_coffee(choosen_item, order_ingredients):
    """Deducts the used ingredients from the available resources and makes coffee."""
    for ingredient, amount in order_ingredients.items():    # OR for ingredient in order_ingredients:
        resources[ingredient] -= amount                     # OR resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {choosen_item}☕ Enjoy!")



# Build drink options for MENU
drinks_menu = list(MENU.keys())     # ['espresso', 'latte' ... ]
valid_drink_choice = [str(i + 1) for i in range(len(drinks_menu))]      # ['1', '2' ... ]

# Create menu string:  MENU --> | 1. Espresso | 2. Latte ... Turn off |
options = drinks_menu + ["report", "turn off"]
menu_string = "MENU --> | " + " | ".join(f"{i + 1}. {option.capitalize()}" for i,option in enumerate(options)) + " |"


# Start the program
while True:
    coffee_machine_is_on = input("Press any key to turn the machine on: ")
    print()

    while coffee_machine_is_on:
        print(menu_string)      # MENU --> | 1. Espresso | 2. Latte ... Turn off |
        user_choice = input('Select a menu item by number: ')
        print()

        # If User choice is a drink, not Report or Turn off
        if user_choice in valid_drink_choice:
            choosen_item = drinks_menu[int(user_choice) - 1]    # Convert back to menu key
            drink_cost = MENU[choosen_item]["cost"]

            # Check resources
            if is_resource_enough(MENU[choosen_item]["ingredients"]):
                print(f"{choosen_item.capitalize()} costs ${drink_cost}")
                money_received = process_coins()
                if is_transaction_successful(money_received, drink_cost):
                    make_coffee(choosen_item, MENU[choosen_item]["ingredients"])


        # Print a report
        elif user_choice == str(len(drinks_menu) + 1):
            for item, amount in resources.items():
                print(f"{item.capitalize()}: {amount}")
            print(f"Money: ${total_money}")

        # Turn off coffee machine
        elif user_choice == str(len(drinks_menu) + 2):
            print("Coffee machine is off. Goodbye!")
            coffee_machine_is_on = False

        # Wrong input
        else:
            print("❌ Wrong input")

        print()



"""
# In this case, if the  User input is not a digit, it won't start from the beginning but from the current coin that has wrong input

def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number.")

quarters = get_valid_int("How many quarters? ")
dimes = get_valid_int("How many dimes? ")
nickles = get_valid_int("How many nickles? ")
pennies = get_valid_int("How many pennies? ")
"""







............................................................................................
../teacher_solution.py

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])






............................................................................................
../art.py








[end]
