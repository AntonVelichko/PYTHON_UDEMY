
##########################################################################################################################
###  DECORATORS  ###


def hello():
	print('hellllooo')
greet = hello()
print(greet)        # hellllooo



---------------



def hello():
	print('hellllooo')
greet = hello
print(greet())      # hellllooo  <--  we have to call it function ()



---------------



def hello():
	print('hellllooo')
greet = hello
print(greet)      # <function hello3 at 0x7016a4d1c9a0>  <--  it shows functioin location



---------------



def hello():
	print('hellllooo')
greet = hello
del hello	    # it deletes hello

print(hello)        # NameError: name 'hello' is not defined
print(hello())      # NameError: name 'hello' is not defined

print(greet())      # hellllooo \n None  <---  func is in memory, reference like 'hello' is deleted, but reference 'greet' is there
                    # python didn't delete the whole function because the function still has another reference 'greet'



---------------



def hello(func):
	func()
	
def greet():
	print('still here!')
	
a = hello(greet)

print(a)        # still here!  \n  None






##########################################################################################################################
###  HIGHER ORDER FUNCTION - HOF  ###

# any func that accept a Function as a paramentr or returns a function

def greet(func):			# this is HOF  <--  func that accepts another function with its paraments
	func()				



---------------



def greet():				# this is HOF  <--  also func that returns other function
	def func():
		return 5
	return func()
	
print(greet())      			# 5

---------------

map(), filter(), reduce() 		# all are HOF






##########################################################################################################################
###  DECORATOR  ###

# a function that wraps another function and enhances it or changes it


def my_decorator(func):
	def wrap_func():
		print('******')
		func()
		print('******')
	return wrap_func


@my_decorator
def hello():
	print('helllooo')


hello()         			# ******
                			# helllooo
                			# ******

@my_decorator				# boostong our func "bye"
def bye():
	print('see ya later')
bye()           			# ******
                			# see ya later
                			# ******



---------------



###  how the Decorator works under the hood  ###

def my_decorator(func):
	def wrap_func():
		print('******')
		func()
		print('******')
	return wrap_func

def hello():
	print('helllooo')

hello2 = my_decorator(hello)		# these 2 lines can be written as "my_decorator(hello)()"
hello2()        			# ******
                			# helllooo
                			# ******


---------------



# hello2 = my_decorator(hello)
# hello2()
# it is the same
my_decorator(hello)()         # ******
                              # helllooo
                              # ******






##########################################################################################################################
###  Decorator with parameter  ###

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



---------------



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



---------------




###  DECORATOR PATTERN  ###
# we can pass as many arguments as we want in wrap function
# this way is better and is the right way
# it gives our decorator flexibility

def my_decorator(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

@my_decorator
def hello(greeting, emoji = ':('):
	print(greeting, emoji)

hello('hiiii')      # hiiii :(




###  @performance  ###

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

---

# modified to find out what is 'args[0]['valid']
user1 = {
    "name": "Sorna",
    "valid": True,
}

user2 = {
    "name": "Sorna",
    "valid": False,  
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            print(args[1]["valid"])     # False
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    return wrapper

@authenticated
def message_friends(*args):
    print("message has been sent")

message_friends(user1, user2)       # message has been sent





