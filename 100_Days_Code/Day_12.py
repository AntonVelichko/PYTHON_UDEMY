##########################################################################################################################
###  exercise Prime Number  ###

............................................................................................
../my_solution.py
import math

def is_prime(num):
    for i in range(1, math.floor(num ** 0.5)):
        if num % (i+1) == 0:
            return False
    return True

'''
🛑 Problem in Your Code
❌ You start your loop at i = 1 and check num % (i+1)
This means:
- You start dividing by 2, 3, 4, ... — but you never check 1, and you never skip it either.
- Also, you check num % 1 == 0 for every number, which is always true, so it wrongly returns False for every input.
'''



............................................................................................
../AI_solution.py
  
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):  # Only odd numbers
        if num % i == 0:
            return False
    return True








##########################################################################################################################
###  XXXXXXX PROJECT  ###

............................................................................................
../my_solution.py








............................................................................................
../teacher_solution.py








............................................................................................
../art.py








[end]
