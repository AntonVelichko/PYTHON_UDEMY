
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


# checking if input is a number
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

    # checking if First Number is a number
    if first_number:
        first_number
    else:
        while not is_number(first_number):
            first_number = input("Enter first number: ")
            if not is_number(first_number):
                print("This is not a number. Enter only number")

    # checking if Operation Sign is correct
    while operation_sign not in operation_signs:
        for key in operations:
            print(key)
        operation_sign = input(f"Enter operator {', '.join(f'"{w}"' for w in operation_signs)} : ")
        if operation_sign not in operation_signs:
            print("Invalid operator. Please try again")

    # checking if Second Number is a number
    while not is_number(second_number):
        second_number = input("Enter second number: ")
        if not is_number(second_number):
            print("This is not a number. Enter only number")

    # converting numbers into float
    first_number = float(first_number)
    second_number = float(second_number)

    # do calculations
    calculation_result = operations[operation_sign](first_number, second_number)

    # printing calculation result
    print(f"{first_number} {operation_sign} {second_number} = {calculation_result}")

    # asking a User to keep result or start over
    keep_result = input(f"Type 'y' to continue with {calculation_result}, or any key to start new: ")

    # remove previous Operation Sign
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
../my_solution.py UPDATED with ChatGPT

from art import logo

# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "❌ Error: Cannot divide by zero\n"
    return n1 / n2

# Check if input is a valid number
def is_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

# Supported operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main calculator function
def calculator():
    first_number = ''
    new_session = True  # Flag to determine when to show the logo

    while True:
        # Show logo only at the start of a new session (not after errors or chaining)
        if new_session:
            print(logo)
            new_session = False  # Don't show it again until the user fully resets

        # Ask user for the first number until valid
        while not is_number(first_number):
            first_number = input("Enter first number: ")
            if not is_number(first_number):
                print("❌ This is not a number. Please enter a valid number.")
        first_number = float(first_number)

        # We are now ready to do calculations with this number
        continue_calculating = True  # This controls the inner calculation loop

        while continue_calculating:
            # Display available operation symbols
            print("\nAvailable operations:")
            for symbol in operations:
                print(f"  {symbol}")

            # Ask user for a valid operator
            operation_sign = ''
            while operation_sign not in operations:
                operation_sign = input(f"Choose an operator {', '.join(operations.keys())}: ")
                if operation_sign not in operations:
                    print("❌ Invalid operator. Try again.")

            # Ask for the second number until valid
            second_number = ''
            while not is_number(second_number):
                second_number = input("Enter second number: ")
                if not is_number(second_number):
                    print("❌ This is not a number. Please enter a valid number.")
            second_number = float(second_number)

            # Perform the calculation using the selected operation
            result = operations[operation_sign](first_number, second_number)

            # If result is an error (like divide by zero), show message and reset
            if isinstance(result, str):
                print(result)
                first_number = ''       # Reset number input
                new_session = False     # Still in same session, don't show logo
                break                   # Exit the inner loop and restart
            else:
                # Show result with 2 decimal places
                print(f"\n✅ {first_number} {operation_sign} {second_number} = {result:.2f}")

            # Ask user if they want to continue with the result
            keep_going = input(f"\nType 'y' to continue calculating with {result:.2f}, or any other key to start over: ")
            if keep_going.lower() == 'y':
                first_number = result       # Keep result as first number
            else:
                print("\n" * 3)
                first_number = ''           # Reset inputs
                new_session = True          # Show logo again next time
                continue_calculating = False  # Exit inner loop

            # If use calculator() that is what will happen
            # A new instance of the function is added to the call stack.
            # The previous instance is still in memory, waiting for the new one to finish.
            # If the user restarts over and over again, you eventually build up many layers of function calls
            # else:
            #     print("\n" * 3)
            #     calculator()  # recursive call

# Run the calculator
calculator()






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




[end]
