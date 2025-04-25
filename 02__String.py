##########################################################################################################################
###  STRINGS  ###


long_string = '''
WOW
0 0
---
'''

print(long_string)

print("example")



print('i' in 'hi')                # True
print('a' not in 'bc')            # True






##########################################################################################################################
###  STRING CONCATENATION  ###
print('hi' + '!')           # hi!
print('hi' + 5)             # gives Error
print('hi' + str(5))        # hi5






##########################################################################################################################
###  ESCAPE SEQUENCE  ###
weather = "it's sunny"
weather = 'it\'s sunny'               # escape sequence
sunny = '\t it is sample'             # Tab
rain = 'new \n stroke'                # new license






##########################################################################################################################
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






##########################################################################################################################
###  STRING INDEX  ###
str = 'abcdefghij'
         #0123456789

# string[start:stop:stepover]
print(str[1:4])            # bcd
print(str[1:])             # bcdefghij
print(str[:])              # abcdefghij
print(str[::])             # abcdefghij
print(str[::1])            # abcdefghij
print(str[1:100])          # bcdefghij
print(str[-1])             # j 
print(str[-4])             # g
print(str[:-3])            # abcdefg
print(str[-3:])            # hij
print(str[::-1])           # jihgfedcba  (revrese)
print(str[::-2])           # jhfdb  (reverse, skip every 2)






##########################################################################################################################
###  BUILT-IN FUNCTIONS  ###
# https://docs.python.org/3/library/functions.html

greet = 'abcde'
print(greet[0:len(greet)])    # abcde
print(greet[0:len(greet)-1])    # abcd






##########################################################################################################################
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






##########################################################################################################################
###  END  ###
print("Studytonight")                     # Studytonight
print("is awesome")                       # is awesome

print("Studytonight",)                    # Studytonight
print("is awesome")                       # is awesome

print("Studytonight", end = "\n")          # Studytonight
print("is awesome")                       # is awesome


print("Studytonight", end =' ')
print("is awesome")                       # Studytonight is awesome

print("Studytonight", end ='')
print("is awesome")                       # Studytonightis awesome

print("Hi", end ='_Studytonight_')
print("you are awesome")                  # Hi_Studytonight_you are awesome



##########################################################################################################################
###  SEP  ###
print("Study", "tonight")                 # Study tonight
print("Study", "tonight", sep = ' ')      # Study tonight

print("Study", "tonight", sep = '')       # Studytonight
print("Study", "tonight", sep = '-&-')    # Study-&-tonight

print("Studytonight","has","been","created","for", sep = "-", end="__STUDENTS__")         # Studytonight-has-been-created-for__STUDENTS__






*************************************************************************************************************************
***  EXERCISE  ***

birth_year = input('What year were you born?')
age = 2025 - int(birth_year)

print(f'your age is: {age}')




***  EXERCISE  ***

name = input('What\'s username ')
password = input('Your password ')
password_length = len(password)
hide = '*' * password_length
print(f'{name}, your password {hide} is {password_length} letters long')





-
