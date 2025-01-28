
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
print(bool(0))                # False
print(bool(None))             # False
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

name = input('What \'s username')
passw = input('Your password')
length = len(passw)
hide = '*' * length
print(f'{name}, your password {hide} is {length} letters long')


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






##########################################################################################################################
###  STRINGS  ###


long_string = '''
WOW
0 0
---
'''

print(long_string)

print("example")




###  STRING CONCATENATION  ###
print('hi' + '!')           # hi!
print('hi' + 5)             # gives Error
print('hi' + str(5))        # hi5




###  ESCAPE SEQUENCE  ###
weather = "it's sunny"
weather = 'it\'s sunny'               # escape sequence
sunny = '\t it is sample'             # Tab
rain = 'new \n stroke'                # new license




###  FORMATTED STRINGS  ###
name = 'John'
age = 5
print('hi ' + name + ' ' +str(age) + ' years old')            # hi John 5 years old
print(f'hi {name} {age} years old')                           # hi John 5 years old (most easy way)
print('hi {} {} years old'.format('Mike', '10'))              # hi Mike 10 years old
print('hi {} {} years old'.format(name, age))                 # hi John 5 years old
print('hi {1} {0} years old'.format(name, age))               # hi 5 John years old
print('hi {n} {a} years old'.format(n = 'Dean', a = 20))      # hi Dean 20 years old

print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))




###  STRING INDEX  ###
python = 'abcdefghij'
         #0123456789

# string[start:stop:stepover]
print(python[1:4])            # bcd
print(python[1:])             # bcdefghij
print(python[:])              # abcdefghij
print(python[::])             # abcdefghij
print(python[::1])            # abcdefghij
print(python[1:100])          # bcdefghij
print(python[-1])             # j 
print(python[-4])             # g
print(python[:-3])            # abcdefg
print(python[-3:])            # hij
print(python[::-1])           # jihgfedcba  (revrese)
print(python[::-2])           # jhfdb  (reverse, skip every 2)




###  BUILT-IN FUNCTIONS  ###
# https://docs.python.org/3/library/functions.html

greet = 'abcde'
print(greet[0:len(greet)])    # abcde
print(greet[0:len(greet)-1])    # abcd




###  STRING METHODS  ###
# https://www.w3schools.com/python/python_ref_string.asp

quote = 'to be or not to be'
print(quote.upper())                # TO BE OR NOT TO BE
print(quote.capitalize())           # To be or not to be
print(quote.lower())                # to be or not to be
print(quote.find('be'))             # 3   /'be' strarts with index 3
print(quote.replace('be', 'me'))    # to me or not to me
print(quote)                        # to be or not to be   / strings are immutable

quote_2 = quote.replace('be', 'me')
print(quote_2)                      # to me or not to me








