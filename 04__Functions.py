
##########################################################################################################################
###  OOP  ###

def say_hello():
  print('hello!')

say_hello()                 # hello!
print(say_hello)            # <function say_hello at 0x7f413b6461f0>
print(say_hello())          # hello!   
                            # None  <--  returns 'None' since the function doesn't have a Return






##########################################################################################################################
###  ARGUMENTS vs PARAMENTRS  ###

def say_hi(name, emoji):                # name, emoji are parameters; used when we define a function
  print(f'hi {name} {emoji}')

say_hi('Anton', 'happy')                # hi Anton happy  <--  'Anton', 'happy' are arguments' used when we call (or invoke) the function




###  POSITIONAL ARGUMENTS  ###
say_hi('sad', 'Bibi')                   # hi sad Bibi


# keyword argument (bad practice, complicates the code)
say_hi(emoji = 'sad', name = 'Bibi')   # hi Bibi  sad


# default parameters
def say_greetings(name = 'Voland', emoji = 'Angry'):
  print(f'hi {name} {emoji}')

say_greetings(emoji = 'Scary')          # hi Voland Scary
say_greetings('Max')                    # hi Max Angry






##########################################################################################################################
###  RETURN  ###

# func should do one thing really well
# func should return something

def sum(num1, num2):
  return num1 + num2

print(sum(4,5))                          # 9

total = sum(10,5)
print(sum(10, total))                    # 25

print(sum(10,sum(10,5)))                 # 25



--------------



def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func(num1, num2)

total = sum(5, 10)
print(total)                              # 15
print(another_func(5, 10))                # NameError: name 'another_func' is not defined



def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func

total = sum(5, 10)
print(total)              # <function sum.<locals>.another_func at 0x7ffb7428fa60>



def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func

total = sum(5, 10)
print(total(10, 20))                      # 30



# after the 'return' function stops executing code
# if you put print(), 'print' will not execute






*************************************************************************************************************************
***  EXERCISE  ***

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit of having checkDriverAge() instead of copying and pasting the function every time?

def check_driver_age():
  age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

check_driver_age()



#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


def check_driver_age(age = 0):
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

check_driver_age(92)






##########################################################################################################################
###  DOCSTRINGS  ###

def test(a):
  '''
  Info: this fuction test and prints param
  '''
  print(a)

test('!')            # !
help(test)            # test(a) Info: this fuction test and prints param
print(test.__doc__)   # Info: this fuction test and prints param






##########################################################################################################################
###  CLEAN CODE  ###

# 1st iteration
def is_even(num):
  if num % 2 == 0:
    return True
  elif num % 2 !=0:
    return False
print(is_even(50))


# 2nd iteration
def is_even(num):
  if num % 2 == 0:
    return True
  return False
print(is_even(51))


# 3rd iteration
def is_even(num):
  return  num % 2 == 0
print(is_even(51))






##########################################################################################################################
###  *ARGS  **KWARGS  ###

# *args - can be anything
# **kwargs - can be keywords
# Rule of the order: params, *args, default parameters, **kwargs  ( name, *args, n = 'abc', **kwasrgs )

def super_func(*args):        # can accept any number as many as we want
  print(*args)                # 1 2 3
  print(args)                 # (1, 2, 3)  <--  tuple
  return sum(args)            # 6
print(super_func(1,2,3))



def super_func(*args, **kwargs):
  print(kwargs)                         # {'num1': 10, 'num2': 20}  <--  dict
  return sum(args)                      # 6
print(super_func(1,2,3, num1 = 10, num2 = 20)) 



def super_func(*args, **kwargs):
  total = 0                         
  for items in kwargs.values():
    total += items
  return sum(args) + total
print(super_func(1,2,3, num1 = 10, num2 = 20))     # 36



def super_func(*args, **kwargs):
  total = 0                         
  for items in kwargs.values():
    print(items)                    # 10        -> next iteration -> 20
    print(kwargs.values())          # dict_values([10, 20]) ->  dict_values([10, 20])
    print(kwargs)                   # {'num1': 10, 'num': 20}   ->  {'num1': 10, 'num': 20}
    total += items
  return sum(args) + total
print(super_func(1,2,3, num1 = 10, num = 20))     # 36




*************************************************************************************************************************
***  EXERCISE  ***

def highest_even(li):
  num = 0
  for item in li:
    if item % 2 == 0 and item > num:
      num = item
  return num

print(highest_even([1,2,10,13,3,4,11]))



###  TEACHER SOLUTION  ###
def highest_even2(arr):
  list_evens = []
  for item in arr:
    if item % 2 == 0:
      list_evens.append(item)
  return max(list_evens)

print(highest_even2([1,2,10,13,3,4,11]))











# 90 scope
# what variables do I have access to?

def some_func():
  total = 100
print(total)              # NameError: name 'total' is not defined



# 91 scope rules
a = 1
def func():
  a = 5
  return a

print(a)                    # 1
print(func())               # 5

#1 - start with local
#2 - parent local scope
#3 - global
#4 - built-in python functions



# 92 global total

total = 0
def count():
  total = 0
  total += 1
  return total

count()
count()
print(count())                  # 1


total_1 = 0
def count_1():
  global total_1                # not a good way to use, hard to understand
  total_1 += 1
  return total_1

count_1()
count_1()
print(count_1())                # 3


total_2 = 2
def count_2(total_2):
  total_2 = 0
  return total_2
print(count_2(total_2))         #0


total_3 = 3
def count_3(total_3):
  #total_3 = 0
  return total_3
print(count_3(total_3))         #3


total_3 = 3
a = 2
def count_3(total_3):
    return total_3
print(count_3(a))         #2


def count_4(total_4):
  total_4 +=1
  return total_4
print(count_4(total_4))         # name 'total_4' is not defined


total_5 = 5
def count_5(total_5):
  total_5 +=1
  return total_5
print(count_5(total_5))         # 6
print(count_5(total_5))         # 6


total_6 = 0
def count_6(total_6):
  total_6 +=1
  return total_6
print(count_6(count_6(count_6(total_6))))        # 3



# 93 nonlocal Keyword
# nonlocal and global make code complicated
def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner:', x)

  inner()                         # inner: nonlocal
  print('outer:', x)
outer()                           # outer: nonlocal


def outer_2():
  x = 'local'
  def inner():
    x = 'nonlocal'
    print('inner:', x)

  inner()                         # inner: nonlocal
  print('outer:', x)
outer_2()                         # outer: local




#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')


.
