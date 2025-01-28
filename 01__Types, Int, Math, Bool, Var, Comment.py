
##########################################################################################################################
###  FUNDAMENTAL DATA TYPES  ###

int
float                                     # https://www.youtube.com/watch?v=PZRI1IfStY0
bool
str
list
dict
tuple
set
complex                                   # for complex math
None                                      # absence of value


a = None
print(a)			                            # None


# Classes                                 <--  custom types
# Specialized Data Types                  <--  libraries, packages (modules)




###  TYPE CONVERSION  ###
print(type(str(100)))       # <class 'str'>
print(type(int('5')))       # <class 'int'>



# https://www.geeksforgeeks.org/python-int-function/




###  TYPE  ###
print(type(6))            # <class 'int'>
print(type(0))            # <class 'int'>
print(type(2/4))          # <class 'float'>
print(type(4/2))          # <class 'float'>
print(4/2)                # 2.0
print(type(9.9 + 1.1))    # <class 'float'>
print(9.9 + 1.1)          # 11.0
print(type(10.56))        # '10' stores in one memory and '56' in another






##########################################################################################################################
###  BOOLEANS  ###

# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
print(bool(0))                # False
print(bool(None))             # False
print(bool())                   # False
print(bool(-1))               # True
print(bool('a'))              # True

year = input('What\'s your birth year?')
age = 2021 - int(year)
print(f'Your age is {age}')
# age = 2021 - bool(year)   -->  2021 - 1






##########################################################################################################################
###  COMMENTS  ###
# https://realpython.com/python-comments-guide/
# self-explanatory

'''
If I really hate pressing `enter` and
typing all those hash marks, I could
just do this instead
'''






##########################################################################################################################
###  MATH OPERATORS  ###
print(2 ** 3)             # 8
print(3 // 2)             # 1   /rounded down to integer
print(5 % 4)              # 1   /modulo, the remainder of the division



###  MATH FUNCTIONS  ###
# https://www.programiz.com/python-programming/modules/math
print(round(3.5))         # 4
print(abs(-1))            # 1



###  OPERATOR PRECEDENCE  ###
#  ()   >>   **   >>   */   >>   +-
print((5 + 4) * 10 / 2)     # 45.0
print(((5 + 4) * 10) / 2)   # 45.0
print((5 + 4) * (10 / 2))   # 45.0
print(5 + (4 * 10) / 2)     # 25.0
print(5 + 4 * 10 // 2)      # 25



###  AUGMENTED ASSIGNMENT OPERATOR  ###

value = 5
value = value + 2         # 7

value += 2
value -= 2
value *= 2
value /= 2




###  BUILD-IN FUNCTIONS  ###
# https://docs.python.org/3/library/functions.html






##########################################################################################################################
###  BINARY  ###
print(bin(5))             # 0b101
print(int('0b111', 2))    # 7






##########################################################################################################################
###  VARIABLES  ###
# keywords  -  https://www.w3schools.com/python/python_ref_keywords.asp

# snake_case
# start with lowercase or 
# start with _underscore means the variable is private (do not change it)
# contains letters, numbers, underscores
# case sensitive
# don't overwrite keywords
# variables are descriptive




###  CONSTANTS  ###
#  all in the capital, the value shouldn't be changed
PI = 3.14                 # Uppercase means to not reassign var



iq = 100                  # statement
user_age = iq / 5         # iq / 5                    <<--  this is expresion 
                          # user_age = iq / 5         <<--  this is statement



a,b,c = 1,2,3
print(a)                  # 1
print(b)                  # 2
print(c)                  # 3







_
