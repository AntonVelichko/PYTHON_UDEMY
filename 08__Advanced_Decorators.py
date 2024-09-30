###
# @classmethod
# @staticmethod

def hello1():
	print('hellllooo')
greet = hello1()
print(greet)        # hellllooo

---

def hello2():
	print('hellllooo')
greet = hello2
print(greet())      # hellllooo

---

def hello3():
	print('hellllooo')
greet = hello3
print(greet)      # <function hello3 at 0x7016a4d1c9a0>  |  functioin location

---

def hello():
	print('hellllooo')
greet = hello
del hello
print(greet())      # hellllooo  | func is in memory but reference like 'hello' is deleted, but reference 'greet' is there
                    # python didn't delete whole function becasue the function stil have another reference 'greet'
print(hello)        # name 'hello' is not defined
print(hello())      # # name 'hello' is not defined

---

def hello(func):
	func()
	
def greet():
	print('still here!')
	
a = hello(greet)

print(a)        # still here!



------------------------------------------------------------------------------------------------------------------------------------



### HIGHT Order Function - HOF
# any func that accept a Function as a paramentr or returns a function

def greet(func):
	func()		# this is HOF

---

def greet():
	def func():
		return 5
	return func()
	
print(greet())      # 5

---

map(), filter(), reduce() - are HOF



------------------------------------------------------------------------------------------------------------------------------------



### DECORATOR - a function that wraps another function and inchanses it or changes it

def my_decorator(func):
	def wrap_func():
		print('******')
		func()
		print('******')
	return wrap_func

@my_decorator
def hello():
	print('helllooo')
hello()         # ******
                # helllooo
                # ******

@my_decorator
def bye():
	print('see ya later')
bye()           # ******
                # see ya later
                # ******

---

# how the Decorator works under the hood

def my_decorator(func):
	def wrap_func():
		print('******')
		func()
		print('******')
	return wrap_func

def hello():
	print('helllooo')

hello2 = my_decorator(hello)
hello2()        # ******
                # helllooo
                # ******

---

# hello2 = my_decorator(hello)
# hello2()
# it is the same
my_decorator(hello)()         # ******
                              # helllooo
                              # ******

---

def my_decorator(func):
	def wrap_func(x):
		print('******')
		func(x)
		print('******')
	return wrap_func

@my_decorator
def hello(greeting):
	print(greeting)

hello('hiiii')      # ******
                    # hiiii
                    # ******

---

# we can give 2 parameters but it is hectic to change them if needed
def my_decorator(func):
	def wrap_func(x, y):
		print('******')
		func(x, y)
		print('******')
	return wrap_func

@my_decorator
def hello(greeting, emoji):
	print(greeting, emoji)

hello('hiiii', ';)')	# ******
                    	# hiiii  ;)
                    	# ******

---

# DECORATOR PATTERN - we can pass as many arguments as we want in wrap function
# this way is better and is a right way

def my_decorator(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

@my_decorator
def hello(greeting, emoji = ':('):
	print(greeting, emoji)

hello('hiiii')      # hiiii :(

---
# @performance

from time import time
def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f'It took {t2 - t1} s')
		return result
	return wrapper


@performance
def long_time():
	for i in range (100000000):
		i * 5

long_time()



----------------------------------------------------------------------------------------------------------------



### EXERCISE

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper

@authenticated
def message_friends(user):
    print("message has been sent")

message_friends(user1)







