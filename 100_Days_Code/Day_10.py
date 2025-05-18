
##########################################################################################################################
###  exercise Leap Year  ###
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
is_leap_year(2000)

---

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


--------------------------------------------------------------------------------------------


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))






##########################################################################################################################
###  PROJECT CALCULATOR  ###

............................................................................................
../my_solution.py
  
# importing logo
from art import logo


# define operations
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# check if input is a number
def is_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False


# signs related to its operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


# initial parameters to check user input (to keep while loop if input is wrong)
operation_signs = ["+", "-", "*", "/"]
first_number = ''
second_number = ''
operation_sign = ''


# program begins
while True:
    print(logo)

    # checking if First number is a number
    if first_number:
        first_number
    else:
        while not is_number(first_number):
            first_number = input("Enter first number: ")
            if not is_number(first_number):
                print("This is not a number. Enter only number")

    # checking if Operation sign is correct
    while operation_sign not in operation_signs:
        for key in operations:
            print(key)
        operation_sign = input(f"Enter operator {', '.join(f'"{w}"' for w in operation_signs)} :")
        if operation_sign not in operation_signs:
            print("Invalid operator. Please try again")

    # checking if Second number is a number
    while not is_number(second_number):
        second_number = input("Enter second number: ")
        if not is_number(second_number):
            print("This is not a number. Enter only number")

    # converting numbers to float
    first_number = float(first_number)
    second_number = float(second_number)

    # do calculations
    calculation_result = operations[operation_sign](first_number, second_number)

    # printing calculation result
    print(f"{first_number} {operation_sign} {second_number} = {calculation_result}")

    # asking a User to keep result or start over
    keep_result = input(f"Type 'y' to continue with {calculation_result}, or any key to start new: ")
    operation_sign = None

    # keep First number if User wants or restart if not
    if keep_result.lower() == "y":
        first_number = calculation_result
        second_number = ''
    else:
        first_number = ''
        second_number = ''
        print("\n" * 20)




............................................................................................
../teacher_solution.py

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()




............................................................................................
../art.py

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



.
