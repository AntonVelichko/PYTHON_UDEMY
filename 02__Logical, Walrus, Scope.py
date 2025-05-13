
##########################################################################################################################
###  IF, ELIF, ELSE  ###


is_old = False
is_licenced = True

if is_old:
  print('Old enough')           # Old enough (if True)
elif is_licenced:
  print('Can drive!')
else:
  print('Not!')                 # check (if False)



###  AND  ###
you_old = True
you_licenced = True
if you_old and you_licenced:
  print('Old and licenced')     # Old enough (if True)
else:
  print('Not!')                 # check (if False)






##########################################################################################################################
###  TERNARY OPERATOR  ###
# conditional expression

is_friend = False
true_friend = 'Yes, friend'  if is_friend else 'Not a friend'
print(true_friend)  # Not a friend






##########################################################################################################################
###  SHORT CIRCUITING  ###

is_Friend = True
is_User = True

if is_Friend or is_User:            # this is short-circuiting because if is_Friend is True then the program stops because after 'or' we don't need to check anymore
  print('Best friend')



--------------



is_Friend = False
is_User = True

if is_Friend and is_User:            # this is short-circuiting because if is_Friend is False then the program stops because after 'and' we don't need to check anymore
  print('Best friend')






##########################################################################################################################
###  LOGICAL OPERATORS  ###
#   <   >   ==   <=   >=   !=   and   or   not   and not
# focus on readability of your code not to write less lines of code and do smart tricks
# better to solve the problem in a simple manner

print(1 < 2 < 3 < 4)                         # True
print(not(True))                             # False
print(not True)                              # False






*************************************************************************************************************************
***  EXERCISE  ***

is_magician = True
is_expert = False

if is_magician and is_expert:
  print('you are a master')
elif  is_magician and not is_expert:
  print('get expert')                         # get expert
elif not is_magician:
  print('need magic')


# this option is shorter but might be a bit complicated for other programmers to read
if is_magician and is_expert:
  print('you are a master')
elif  is_magician or is_expert:               # short-circuiting
  print('at least you are getting there')






##########################################################################################################################
###  IS vs ==  ###

print(True == 1)            # True
print('1' == 1)             # False
print([] == 1)              # False
print([] == 0)              # False
print(10 == 10.0)           # True
print([] == [])             # True
print([1,2,3] == [1,2,3])   # True
print((1,2,3) == (1,2,3))   # True
print((1,2,3) == (3,2,1))   # False
print({1,2,3} == {3,2,1})   # True



# 'is' checks if the value is stored in one memory location
print(True is 1)            # False
print('1' is 1)             # False
print([] is 1)              # False
print(10 is 10.0)           # False
print([1,2,3] is [1,2,3])   # False  /every list (dict, sets, tuples) in its own memory location
print([] is [])             # False  /every list (dict, sets, tuples) in its own memory location

print('1' is '1')           # True
print(True is True)         # True
print(10 is 10)             # True



a = [1,2,3]
b = [1,2,3]
print(a is b)               # False
print(a == b)               # True


a = [1,2,3]
b = a                       # refference in memory
print(a is b)               # True



# place in memory
print(id('string'))         # 132055321746688
print(id(123))              # 132055322215432






##########################################################################################################################
###  WALRUS OPERATOR  ###

a = 'Helloooooooo'

if (len(a) > 10):
  print(f'too long {len(a)} elements')          # too long 12 elements

if ((n := len(a)) > 10):                        # 'n' equals of expression 'len(a)'
  print(f'too long {n} elements')

b = len(a)
if (b > 10):
  print(f'too long {b} elements')
  

while((n := len(a)) > 1):
  print(n)
  a = a[:-1]
print(a)






##########################################################################################################################
###  SCOPE  ###
# what variables do I have access to?


def some_func():
  total = 100
print(total)                         # NameError: name 'total' is not defined



if False:
  x = 10
print(x)                              # 10
                                      # if Flase  <--  NameError: name 'x' is not defined





###  SCOPE RULES  ###

#1 - start with local
#2 - parent local scope
#3 - global
#4 - built-in python functions



a = 1
def func():
  a = 5
  return a

print(a)                             # 1
print(func())                        # 5  <--  #1 - start with local



a = 1
def func():
  return a

print(a)                             # 1
print(func())                        # 1  <--  using global variable



--------------



a = 1
def parent():
  a = 10
  def func():
    return a
  return func()

print(a)                             # 1
print(parent())                      # 10  <--  #2 - parent local scope



a = 1
def parent():
  def func():
    return a
  return func()

print(a)                              # 1
print(parent())                       # 1  <--  #3 - global



--------------



a = 1
def parent():
  def func():
    return sum
  return func()

print(a)                              # 1
print(parent())                       # <built-in function sum>  <--  #4 - built-in python functions






###  GLOBAL KEYWORD  ###

total = 0
def count():
  total = 0
  total += 1
  return total

count()
count()
print(count())                          # 1  <--  every time we run a function we reset 'total' to '0'




# global keyword
# better not use "global', only use if really nessecary
total = 0
def count():
  global total                          # not a good way to use, hard to understand
  total += 1
  return total

count()
count()
print(count())                          # 3




# dependency injection (without using a global variable)
total = 0
def count(total):
  total +=1
  return total
print(count(count(count(total))))        # 3





###  NONLOCAL KEYWORD  ###

# nonlocal and global make code complicated
# nonlocal is used to refer to Parent local
# try to make you code predictable; not using 'nonlocal' or 'global'

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
  # nonlocal x
    x = 'nonlocal'
    print('inner:', x)

  inner()                         # inner: nonlocal
  print('outer:', x)
outer_2()                         # outer: local




def outer_3():
  x = 'local'
  def inner():
    nonlocal x
    # x = 'nonlocal'
    print('inner:', x)

  inner()                         # inner: local
  print('outer:', x)
outer_3()                         # outer: local



.

