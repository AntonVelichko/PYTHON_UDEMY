# 79 functions
def say_hello():
  print('hello!')

say_hello()                 # hello!
print(say_hello)            # <function say_hello at 0x7f413b6461f0>
print(say_hello())          # hello!   # None



--------------------------------------------------------------------



# 80 parameters and arguments
def say_hi(name, emoji):
  print(f'hi {name} {emoji}')

say_hi('Anton', 'happy')                # hi Anton happy


# 81 positional arguments
say_hi('sad', 'Bibi')                   # hi sad Bibi

# keyword argument (bad practice, complicate the code)
say_hi(emoji = 'sad', name = 'Bibi')   # hi Bibi  sad


# default parameters
def say_greetings(name = 'Voland', emoji = 'Angry'):
  print(f'hi {name} {emoji}')

say_greetings(emoji = 'Scary')          # hi Voland Scary



--------------------------------------------------------------------



# 82 return
def sum(num1, num2):
  return num1 + num2

print(sum(4,5))                          # 9

# func should do one thing really well
# func should return something

total = sum (10,5)
print(sum(10, total))                    # 25

print(sum(10,sum(10,5)))                 # 25



--------------------------------------------------------------------



def sum(num1, num2):
  def another_func(num1,num2):
    return num1 + num2
  return another_func(num1,num2)

total = sum(5, 10)
print(total)                              # 15


def sum(num1, num2):
  def another_func(num1,num2):
    return num1 + num2
  return another_func

total = sum(5, 10)
print(total)              # <function sum.<locals>.another_func at 0x7ffb7428fa60>


def sum(num1, num2):
  def another_func(num1,num2):
    return num1 + num2
  return another_func

total = sum(5, 10)
print(total(10, 20))                      # 30


# after 'return' function stops execute code



--------------------------------------------------------------------



# 83 Exercise: Tesla
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

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
  #age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

check_driver_age(92)


