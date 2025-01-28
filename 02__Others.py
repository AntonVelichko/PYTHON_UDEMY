
# 60 if elif else
is_old = False
is_licenced = True

if is_old:
  print('Old enough')           # Old enough (if True)
elif is_licenced:
  print('Can drive!')
else:
  print('Not!')                 # check (if False)

you_old = True
you_licenced = True
if you_old and you_licenced:
  print('Old and licenced')     # Old enough (if True)
else:
  print('Not!')                 # check (if False)



--------------------------------------------------------------------







# 63 Ternary operator
is_friend = False
true_friend = 'Yes, True'  if is_friend else 'No friend'
print(true_friend)  # No friend



# 64 Short-circuiting

# 65 Logical operators
# > < ==  !=  and  or  not
print(1 < 2 < 3 < 4)    # True
print(not(True))        # False
print(not True)         # False


# 66 Exercise
is_magician = True
is_expert = False

if is_magician and is_expert:
  print('you are a master')
elif  is_magician and not is_expert:
  print('get expert')                         # get expert
elif not is_magician:
  print('need magic')



--------------------------------------------------------------------



# 67 is vs ==
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
print([] is [])             # False
print([1,2,3] is [1,2,3])   # False
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



--------------------------------------------------------------------



# 72 enumerate()
for char in enumerate('abc'):
  print(char)                       # (0, 'a')  /  (1, 'b')  /  (2, 'c')

for i, char in enumerate('abc'):
  print(i, char)                    # 0 a  /  1 b  /  2 c

for i, char in enumerate(list(range(10))):
  if char == 5:
    print(f'index of 5 is: {i}')    # index of 5 is: 5




--------------------------------------------------------------------



# end
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



# sep
print("Study", "tonight")                 # Study tonight
print("Study", "tonight", sep = ' ')      # Study tonight

print("Study", "tonight", sep = '')       # Studytonight
print("Study", "tonight", sep = ' & ')    # Study & tonight

print("Studytonight","has","been","created","for", sep = "_", end="*STUDENTS")
# Studytonight_has_been_created_for*STUDENTS



--------------------------------------------------------------------



# 85 docstrings
def test(a):
  '''
  Info: this fuction test and prints param
  '''
  print(a)

test('!')            # !
help(test)            # test(a) Info: this fuction test and prints param
print(test.__doc__)   # Info: this fuction test and prints param



# 86 clean code
def is_even(num):
  if num % 2 == 0:
    return True
  elif num % 2 !=0:
    return False
print(is_even(50))


def is_even(num):
  if num % 2 == 0:
    return True
  return False
print(is_even(51))


def is_even(num):
  return  num % 2 == 0
print(is_even(51))



# 87 .*args  **kwargs
# *args - can be anything
# **kwargs - can be keywords
def super_func(*args):        # can accept any number as many as we want
  print(args)                 # (1, 2, 3)  /tuple
  return sum(args)            # 6
print(super_func(1,2,3))


def super_func(*args, **kwargs):
  print(kwargs)                         # {'num1': 10}  /dict
  return sum(args)                      # 6
print(super_func(1,2,3, num1 = 10))


def super_func(*args, **kwargs):
  total = 0                         
  for items in kwargs.values():
    total += items
  return sum(args) + total
print(super_func(1,2,3, num1 = 10))     # 16


def super_func(*args, **kwargs):
  total = 0                         
  for items in kwargs.values():
    print(items)                    # 10        -> next iteration -> 20
    print(kwargs.values())          # dict_values([10, 20]) ->  dict_values([10, 20])
    print(kwargs)                   # {'num1': 10, 'num': 20}   ->  {'num1': 10, 'num': 20}
    total += items
  return sum(args) + total
print(super_func(1,2,3, num1 = 10, num = 20))     # 36

# Order of execution: params, *args, default parametrs, **kwargs



# 88 Exercise
def highest_even(li):
  num = 0
  for item in li:
    if item % 2 == 0 and item > num:
      num = item
  return num

print(highest_even([1,2,10,13,3,4,11]))



def highest_even2(arr):
  list_evens = []
  for item in arr:
    if item % 2 == 0:
      list_evens.append(item)
  return max(list_evens)

print(highest_even2([1,2,10,13,3,4,11]))




# 89 walrus operator
a = 'Helloooooooo'

if (len(a) > 10):
  print(f'too long {len(a)} elements')

if ((n := len(a)) > 10):
  print(f'too long {n} elements')

b = len(a)
if (b > 10):
  print(f'too long {b} elements')

while((n := len(a)) > 1):
  print(n)
  a = a[:-1]
print(a)



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
