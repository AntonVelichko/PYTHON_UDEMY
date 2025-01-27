
##########################################################################################################################
### OOP  ###

# OOP combines Data and Functions


class BigObject:
    pass


obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))                      # <class 'dict'>
print(type(obj1))                    # <class '__main__.BigObject'>



--------------



class PlayerCharacter:
    membership = True                # Class Object Attribute (static)

    def __init__(self, name, age):
        self.name = name	        #attributes
        self.age = age

    def run(self):
        print('run')
        #return 'Done'

    def shout(self):
        print(f'My name is {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 20)
player2.attack = 50

print(player1.name)               # Cindy
print(player2.age)                # 20
print(player2.run())              # None - because Funcion has no return, uncomment and will be "Done"
print(player1)                    # <__main__.PlayerCharacter object at 0x75d86f4eb1f0>
print(player2)                    # <__main__.PlayerCharacter object at 0x75d86f51e490>
print(player2.attack)             # 50

print(player1.shout())            # My name is Cindy    # None
print(player2.shout())            # My name is Tom      # None

print(player1.membership)         # True (but it is not dynamic)

help(player1)                     # run it in the program (entire blueprint of the object)
help(list)                        # to see the List blueprint



------------------



class PlayerCharacter:
    membership = True                    # if False --> AttributeError: 'PlayerCharacter' object has no attribute 'name'
    def __init__(self, name, age):
        if(self.membership):             # self refers to this PlayerCharacter
            self.name = name             # can also be used if(PlayerCharacter.membership): instead of if(self.membership):
            self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 20)
player2.attack = 50

print(player1.name)     # Cindy
print(player1.run())    # run
                        # None


---------------



class PlayerCharacter:
    membership = True                                       # if False --> AttributeError: 'PlayerCharacter' object has no attribute 'name'
    def __init__(self, name = 'anonymous', age = 20):       # default parameters
        if(age >= 18 and self.membership):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

player1 = PlayerCharacter('Tom', 18)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.name)         # Tom
print(player1.run())        # Run
                            # None
                            
print(player2.name)         # anonymous






##########################################################################################################################
### @classmethod  ###


class PlayerCharacter:
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod                                # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):         # 'cls' stands for Class , 'cls' is like 'self'
        return num1 + num2


player1 = PlayerCharacter('Tom', 10)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.adding_things(2,3))                    # 5
print(player2.name, player2.age)                     # anonymous 20
print(PlayerCharacter.adding_things(3,4))            # 7
print(player2.adding_things(4,5))                    # 9



-----------------



class PlayerCharacter:
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod                                     # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)             # using 'cls' to instantiate an object


print(PlayerCharacter.adding_things(3,3))            # <__main__.PlayerCharacter object at 0x72fbc215bee0>


player = PlayerCharacter.adding_things(11,11)        # object 'Teddy' instantiated with age = num1 + num2
print(player.age)                                    # 22
print(player.name)                                   # Teddy
print(player)                                        # <__main__.PlayerCharacter object at 0x76e0e7778dd0>






##########################################################################################################################
### @staticmethod  ###

class PlayerCharacter:
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod                            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod                            # same as @classmethod but no access to cls
    def adding_things2(num1, num2):
        return num1 + num2

player = PlayerCharacter.adding_things(11,11)
print(player.age)                            # 22
print(player.name)                           # Teddy






##########################################################################################################################
###   DECORATORS   ###
https://www.makeuseof.com/tag/python-instance-static-class-methods/


###  DECORATOR PATTERNS  ###
class DecoratorExample:                        # Example Class
  def __init__(self):                          # Example Setup  
    print('Hello, World!')

  @staticmethod
  def example_function():                      # This method is decorated!
    print('I\'m a decorated function!')
      
de = DecoratorExample()                         # Hello, World!

de.example_function()                           # I'm a decorated function!
print('---')

DecoratorExample().example_function()           # Hello, World!
print('---')                                    # I'm a decorated function!

DecoratorExample.example_function()             # I'm a decorated function!
print('----')

# Decorators have to immediately precede a function or class declaration
# They start with the @ sign, and unlike normal methods, you don't have to put parentheses on the end unless you are passing in arguments



-----------------



###  INSTANCE METHOD  ###
# The most common type of method in Python classes, no decorator is needed
# When you create a Python class, its methods will be instance methods by default

class DecoratorExample:                        # Example Class
  def __init__(self):                          # Example Setup
    print('Hello, World!')
    self.name = 'Decorator Example'

  def example_function(self):                  # This method is an instance method!
    print('I\'m an instance method!')
    print('My name is ' + self.name)

de = DecoratorExample()                        # Hello, World!
de.example_function()                          # I'm an instance method!
                                               # My name is Decorator Example


-----------------



### STATIC METHOD  ###
# Static methods are methods that are related to a class in some way
# but don't need to access any class-specific data 
# You don't have to use self, and you don't even need to instantiate an instance, you can simply call your method
# The @staticmethod decorator was used to tell Python that this method is a static method

class DecoratorExample:             # Example Class
  def __init__(self):               # Example Setup
    print('Hello, World!') 

  @staticmethod
  def example_function():            # This method is a static method!
    print('I\'m a static method!')

de = DecoratorExample.example_function()    # I'm a static method!

# Static methods are great for utility functions, which perform a task in isolation
# They don't need to (and cannot) access class data
# They should be completely self-contained, and only work with data passed in as arguments
# You may use a static method to add two numbers together or print a given string



-----------------



### CLASS METHOD  ###
# Class methods know about their class
# They can't access specific instance data, but they can call other static methods
# Class methods don't need self as an argument, 
# but they do need a parameter called cls
# This stands for class, and like self, it gets automatically passed in by Python
# Class methods are created using the @classmethod decorator

class DecoratorExample:                     # Example Class
  def __init__(self):                       # Example Setup
    print('Hello, World!') 

  @classmethod
  def example_function(cls):                # This method is a class method!
    print('I\'m a class method!')
    cls.some_other_function()

  @staticmethod
  def some_other_function():
    print('I\'m a static method!')

de = DecoratorExample()                     # Hello, World!
de.example_function()                       # I'm a class method!
                                            # I'm a static method!
de.some_other_function()                    # I'm a static method!

# Remember, instance methods can manipulate an object's state and have access to the class itself via self
# Class methods, on the other hand, can't access the instance of a class but can access the class itself
# This is the major difference between class and instance methods in Python.
# Since class methods can manipulate the class itself, they are useful when you're working on larger, more complex projects






##########################################################################################################################
###  INCAPSULATION  ###


class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('Run')

  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Tony', 99)
player1.speak()                         # My name is Tony, and I am 99 years old
PlayerCharacter('John', 88).speak()     # My name is John, and I am 88 years old

# Without a class we would use 2 variables and 2 functions
# With class we have everything in one place, a blueprint, a package
# This is an entire object I can interact with, I can use



# if there are no methods - it's useless, it's like a dictionary
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('Tony', 99)
print(player1.name)         # Tony
print(player1.age)          # 99

player2 = {'name': 'John', 'age': 100}        # dictionary
print(player2['name'])      # John
print(player2['age'])       # 100

# the difference between player1 and player2 is the access to information






##########################################################################################################################
###  ABSRACTION  ###

# This is an example of abstraction. We have access to the method "count"
# but we don't know how it works and we don't need to know actually
# We just need access to it
print((1,2,3,1).count(1))            # 2


class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('Run')

  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old')
      

player1 = PlayerCharacter('Tony', 99)
player1.name = '!!!'
player1.speak = 'Booo'

print(player1.name)     # !!!
print(player1.speak)    # Booo
print(player1.speak())  # TypeError: 'str' object is not callable






##########################################################################################################################
###  INHERITANCE  ###


class User():
  def sign_in (self):      # if no attributes then we don't need __init__ , we do not initialize anything
    print('Logged in')

class Wizard(User):        # 'class Wizard' INHERITS methods from 'class User'
  pass

class Archer(User):
  pass

wizard1 = Wizard()
wizard1.sign_in()       # Logged in



------------------------------------------------------------------------------------------------------------------------



class User:
  def sign_in (self):                  # if no attributes then we don't need __init__ , we do not initialize anything
    print('Logged in')


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power of {self.power}')


class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def attack(self):
    print(f'Attacking with arrows: arrows left - {self.arrows}')


wizard1 = Wizard('Merlin', 60)
print(isinstance(wizard1, Wizard))    # True  -->  wizard1 inherits methods from class Wizard
print(isinstance(wizard1, User))    # True  -->  wizard1 inherits methods from class User
print(isinstance(wizard1, object))    # True  -->  wizard1 inherits methods even from Object base class
print(isinstance(User, object))        # True






##########################################################################################################################
###  PRIVACY  ###

_<variable name> - means this variable is PRIVATE; do not change it


class PlayerCharacter:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def run(self):
    print('Run')

  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old')
      

player1 = PlayerCharacter('Tony', 99)
player1.name = '!!!'
player1.speak = 'Booo'






##########################################################################################################################
###  POLYMORPHISM  ####  
# many forms
# different object classes can share the same method name


class User:
  def sign_in(self):
    print('Logged in')

  def attack(self):                                      # initial attack function
    print('User attack')


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):                                      # this attack function will override User attack
    print(f'Attacking with power of {self.power}')


class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def attack(self):
    print(f'Attacking with arrows; arrows left - {self.arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)
user1 = User()


def player_attack(char):
  char.attack()


player_attack(wizard1)              # Attacking with power of 60  -->  using 'def player_attack(char):' is Polymorphism
wizard1.attack()                    # Attacking with power of 60  -->  using 'class Wizard(User):'
Wizard('Saruman', 70).attack()      # Attacking with power of 70

player_attack(archer1)              # Attacking with arrows; arrows left - 30  -->  using 'def player_attack(char):' is Polymorphism


# for loop
for char in [wizard1, archer1]:      # Attacking with power of 60  -->  this is Polymorphism
  char.attack()                      # Attacking with arrows: arrows left - 30  -->  this is Polymorphism

player_attack(user1)                 # User attack
user1.attack()                       # User attack



--------------



# when we keep both methods, from inheritance and local
class User:
  def sign_in(self):
    print('Logged in')

  def attack(self):                  # initial attack function
    print('User initial attack')


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):      
    User.attack(self)                # this will keep both class and local Attack
    print(f'Attacking with power of {self.power}')


class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def attack(self):
    print(f'Attacking with arrows: arrows left - {self.arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)
user1 = User()


def player_attack(char):
  char.attack()


player_attack(wizard1)  # User initial attack
                        # Attacking with power of 60
wizard1.attack()        # User initial attack
                        # Attacking with power of 60
player_attack(archer1)  # Attacking with arrows: arrows left - 30


# for loop
for char in [wizard1, archer1]:      # User initial attack  \n  # Attacking with power of 60
  char.attack()                      # Attacking with arrows: arrows left - 30

player_attack(user1)                 # User initial attack






##########################################################################################################################
###  SUPER CLASS  ###


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):      # this shows the ORDER of arguments
        User.__init__(self, email)               # one way to pass argument (more efficient way Andrew says)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)        # merlin@gmail.com



----------



# super()
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)                # reffering to Super Class (class above), no self needed  -->> substitute "User.__init__(self, email)"
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)        # merlin@gmail.com






##########################################################################################################################
###  INTROSPECTION   ### 
# the ability to determine the object at run time  


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(dir(wizard1))     # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',   ...   'attack', 'email', 'name', 'power', 'sign_in']
                        # gives all of the methods and attributes that the Wizard instance has
                        # showing what you have access to






##########################################################################################################################
###  DUNDER METHODS  ###
https://docs.python.org/3/reference/datamodel.html#special-method-names
# we don't write our own Dunder Methods


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
action_figure = Toy('red', 0)

print(action_figure.__str__())  # <__main__.Toy object at 0x773cad9efc90>
print(str(action_figure))       # <__main__.Toy object at 0x773cad9efc90>

# __<name of method>__  is a special "magical" method, can be accessed with 2 ways



-----



class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
    def __str__(self):                  # do not modify Dunder Methods, we modified it now and it acting different way
        return f'{self.color}'


action_figure = Toy('red', 0)
print(action_figure.__str__())          # red  |  'str' is modified only when used with a specific object ('Toy' in our case)
print(str(action_figure))               # red
print(str('action_figure'))             # action_figure
print(str(123) + 'a')                   # 123a
print(type(str(123)))                   #  <class 'str'>



-----



class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]

action_figure = Toy('red', 0)


print(action_figure.__str__())       # red
print(str(action_figure))            # red

print(len(action_figure))            # 5

print(action_figure())               # yes??

print(action_figure['name'])         # Yoyo

print(len('123456789'))              # 9

print(action_figure.__del__())       # deleted
print(del(action_figure))            # SyntaxError: invalid syntax






##########################################################################################################################
###  MULTIPLE INHERITANCE  ###
# Complicates code; be very cautious. Maybe avoid it to use


class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self): 
        User.attack(self)
        print(f'Attacking with power of {self.power}')
        
    def run(self):
        print('Run fast Wazard')            # if we put here "print(f'Run fast {self.name}')"  -->>  "Run fast Borgie" instead of "Run fast Wizard"


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print('Run fast Archer')


class HybridBorg(Wizard, Archer):
    pass

hb1 = HybridBorg('Borgie', 50)      # extentiation

print(hb1.run())                    # Run fast Wizard    |     Order matters; if Archer first in "class HybridBorg(Archer, Wizard)" it will gives 'Run fast Archer'
                                    # None
print(hb1.name)                     # Borgie
print(hb1.power)                    # 50
print(hb1.arrows)                   # showes nothing    |    if we put Archer first in "class HybridBorg(Archer, Wizard)"  -->> 50
print(hb1.check_arrows())           # gives an error since it doesn't know the arrows   |   if we put Archer first in "class HybridBorg(Archer, Wizard)"  -->> 50 remaining  \n  None


# Because of Order Matter and if Wizard first we can't add Arrows to the class HybridBorg it is becoming tricky using multiple inheritance
# Code becomes more complicated to solve that problem with Arrows



-----------



# continue
# the limitation with Arrows is fixed but complicates the code
# multiple inheritance might complicate code a lot (some programming languages don't allow multi-inheritances)


class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self): 
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print('Run fast Archer')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('Borgie', 50, 100)

print(hb1.run())                    # Run fast Archer 
                                    # None
print(hb1.check_arrows())           # 100 remaining  
                                    # None
print(hb1.attack())                 # Attacking with power of 50 
                                    # Order matters; 'def __init__(self, name, power, arrows):'
                                    # in this case, it will be Wizard
                                    # None
print(hb1.sign_in())                # Logged in  
                                    # None






##########################################################################################################################
###  MRO  ###
# Method Resolution Order
# __mro__
# This will be a bad code since it's complicated to understand
# Do not structure your code this way
http://www.srikanthtechnologies.com/blog/python/mro.aspx


class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)    # (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)
print(M.mro())      # same like "print(M.__mro__)"

'''
    object
  ↗     ↑    ↖
 X3     Y4     Z5
  ↖ ↗    ↖ ↗
   A2      B1
      ↖ ↗
       M
'''






*************************************************************************************************************************
***  EXERCISE  ***


#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Barsik', 1)
cat2 = Cat('Alicia', 2)
cat3 = Cat('Murka', 4)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old.')






*************************************************************************************************************************
***  EXERCISE  ***
# Extending List


class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))                 # 1000
print(super_list1)                      # []

super_list1.append(5)                   
print(super_list1[0])                   # 5
print(super_list1)                      # [5]

print(issubclass(SuperList, list))      # True
print(issubclass(list, object))         # True






*************************************************************************************************************************
***  EXERCISE  ***


class Pets():
    animals = []
    
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#1 Add another Cat
class Bob(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon('Simon', 1)
cat2 = Sally('Sally', 2)
cat3 = Bob('Bob', 3)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

#OR  -->  my_cats = [Simon('Simon', 1), Sally('Sally', 2), Bob('Bob', 3)]


#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)


#4 Output all of the cats walking using the my_pets instance
my_pets.walk()                  # Simon is just walking around
                                # Sally is just walking around
                                # Bob is just walking around

print(cat1.sing('Moew'))        # Moew





