
##########################################################################################################################
###  FUNCTION  ###

def say_hello():
  print('hello!')

say_hello()                 # hello!
print(say_hello)            # <function say_hello at 0x7f413b6461f0>
print(say_hello())          # hello!   
                            # None  <--  returns 'None' since the function doesn't have a Return




def my_function(something)      # something is 'parameter'
  do something
  
my_function(123)                # 123 is argument




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
  Info: this function tests and prints param
  '''
  print(a)

test('!')             # !
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





##########################################################################################################################
###  RECURSION  ###
# лучше переписать рекурсию в интерактивном обычном виде после того как мы проверили что метод работает

def nonrecursive_factorial(n):
	result = 1
	for multiplier in range(2, n + 1):
		result *= multiplier
	return result
print(nonrecursive_factorial(5))


---


# Факториалом числа n (обозначается n!) называется произведение
# всех натуральных чисел от 1 до n включительно.

# пример рекурсивной функции
def factorial(n):
    if n == 0:
        return 1  # условие выхода
    else:
        return n * factorial(n - 1)  # рекурсивный вызов

# вычисление факториала числа 5
print(factorial(5))

# факториал от 100 выдаст ошибку тк будет достигнута макс глубина рекурсии
# а если считать факториал обычным способом то мы получим число


---


# Числа Фибоначчи — последовательность, в которой первые два числа равны единице,
# а все последующие — сумме двух предыдущих.


def fib(n):
    if n == 1 or n == 2:  # условие выхода
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # рекурсивный вызов

for i in range(1, 100):
	print(fib(i))
# фиб от 100 будет вычисляться очень долго тк нигде не запоминаются предыдущие числа фибоначи и прога считает для каждого значения каждый раз



# можно исмпольовать кэширование тогда вычисение будет моментальным тк будут запоминаться предыдущие числа фибоначи
# это называется Мемоизация значения
import functools
@functools.lru_cache(maxsize=None)

def fib(n):
    if n == 1 or n == 2:  # условие выхода
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # рекурсивный вызов

for i in range(1, 100):
	print(fib(i))



---



"""
Ханойская башня является одной из популярных головоломок XIX века.
Даны три стержня, на один из которых нанизаны восемь колец, причем
кольца отличаются размером и лежат меньшее на большем. Задача
состоит в том, чтобы перенести пирамиду из восьми колец за наименьшее
число ходов на другой стержень. За один раз разрешается переносить
только одно кольцо, причём нельзя класть большее кольцо на меньшее.
"""


def hanoi(n, a, b, c):
    """Рекурсивный алгоритм решения данной головоломки.
    Данная функция перекладывает n колец со стержня A
    на стержень C, используя B как промежуточный

    :param n:  количество колец
    :param a:  имя первого стержня
    :param b:  имя второго стержня
    :param c:  имя третьего стержня
    :return:   None
    """
    if n != 0:  # если количество колец не равно нулю
        # перенести n - 1 колец из A в B
        hanoi(n - 1, a, c, b)
        # перенести одно кольцо из A в C
        print('Перенести кольцо из', a, 'в', c)
        # перенести n - 1 колец из B в C
        hanoi(n - 1, b, a, c)

# решение задачи для трёх колец
hanoi(3, 'A', 'B', 'C')

.
