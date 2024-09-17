# OOP

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
print(type({}))
print(type(obj1))


----------------------------------------------------------------------


class PlayerCharacter:
    membership = True    # Class Object Attribute (static)

    def __init__(self, name, age):
        self.name = name	#attributes
        self.age = age

    def run(self):
        print('run')
        #return 'Done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 20)
player2.attack = 50

print(player1.name)
print(player2.age)
print(player2.run())    # None - becasue Funcion has no return, uncomment to see difference
print(player1)            # <__main__.PlayerCharacter object at 0x75d86f4eb1f0>
print(player2)            # <__main__.PlayerCharacter object at 0x75d86f51e490>
print(player2.attack)     # 50
help(player1)


----------------------------------------------------------------------


class PlayerCharacter:
    membership = True  # Class Object Attribute (static)
    def __init__(self, name, age):
        if(self.membership):
            self.name = name  #attributes
            self.age = age

    def run(self):
        print('run')
        #return 'Done'


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 20)
player2.attack = 50

print(player1.name)
print(player1.run())


----------------------------------------------------------------------


class PlayerCharacter:
    membership = True  # Class Object Attribute (static)
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name  #attributes
            self.age = age

    def run(self):
        print('Run')
        #return 'Done'


player1 = PlayerCharacter('Tom', 10)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.name)
print(player1.run())


----------------------------------------------------------------------


#Exercise

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
#print(cat1.age)
#print(oldest_cat(cat1.age,cat2.age,cat3.age))

print(f'The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old.')


----------------------------------------------------------------------


#@classmethod and @staticmethod
class PlayerCharacter:
    membership = True  # Class Object Attribute (static)
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name  #attributes
            self.age = age

    def run(self):
        print('Run')
        #return 'Done'

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 10)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(3,3))







class PlayerCharacter:
    membership = True  # Class Object Attribute (static)
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name  #attributes
            self.age = age

    def run(self):
        print('Run')
        #return 'Done'

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


print(PlayerCharacter.adding_things(3,3))    # <__main__.PlayerCharacter object at 0x72fbc215bee0>
# object 'Teddy' instantiated with age = num1 + num2






class PlayerCharacter:
    membership = True  # Class Object Attribute (static)
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name  #attributes
            self.age = age

    def run(self):
        print('Run')
        #return 'Done'

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player = PlayerCharacter.adding_things(3,3)
print(player.age)                            # 6 supposed to give, but give an error



----------------------------------------------------------------------



https://www.makeuseof.com/tag/python-instance-static-class-methods/
# Decorator Patterns
class DecoratorExample:
  # Example Class """
  def __init__(self):
    # Example Setup """
    print('Hello, World!')

  @staticmethod
  def example_function():
    # This method is decorated! """
    print('I\'m a decorated function!')

de = DecoratorExample()

de.example_function()
print('-')
DecoratorExample().example_function()
print('-')
DecoratorExample.example_function()

print('1----')


# Instance Methods
class DecoratorExample:
  # Example Class """
  def __init__(self):
    # Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'

  def example_function(self):
    # This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)

de = DecoratorExample()
de.example_function()

print('2----')


# Static Method
class DecoratorExample:
  # Example Class """
  def __init__(self):
    # Example Setup """
    print('Hello, World!') 

  @staticmethod
  def example_function():
    # This method is a static method! """
    print('I\'m a static method!')

de = DecoratorExample.example_function()


print('3----')

# Class Method
class DecoratorExample:
  # Example Class """
  def __init__(self):
    # Example Setup """
    print('Hello, World!') 

  @classmethod
  def example_function(cls):
    # This method is a class method! """
    print('I\'m a class method!')
    cls.some_other_function()

  @staticmethod
  def some_other_function():
    print('Hello!')

de = DecoratorExample()
de.example_function()






# Incapsuation
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('Run')

  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Tony', 99)
player1.speak()

PlayerCharacter('John', 88).speak()


# if no methods - it's useless
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('Tony', 99)
print(player1.name)
print(player1.age)

player2 = {'name': 'Tony', 'age': 100}
print(player2['name'])
print(player2['age'])







# Absraction

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('Tony', 99)
player1.name = '!!!'
player1.speak = 'Booo'

print(player1.speak)    # Booo
print(player1.speak())  # Object is not callable







# Inheritance

class User:

  def sign_in(
      self
  ):  # if no attributes then we don't need __init__ , we do not initialize anything
    print('Logged in')

class Wizard(User):
  pass

class Archer(User):
  pass

wizard1 = Wizard()
wizard1.sign_in()


--------------------------------------------------


class User:

  def sign_in(
      self
  ):  # if no attributes then we don't need __init__ , we do not initialize anything
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
print(isinstance(wizard1, Wizard))    # True, wizard1 inherits methods from class Wizard
print(isinstance(wizard1, User))    # True, wizard1 inherits methods from class User
print(isinstance(wizard1, object))    # True, wizard1 inherits methods even from Object base class



--------------------------------------------------



# Polumorphism
class User:

  def sign_in(self):
    print('Logged in')

  def attack(self):  # initial attack function
    print('Do nothing')


class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):  # this attack function will override User attack
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


player_attack(wizard1)  # Attacking with power of 60
player_attack(archer1)  # Attacking with arrows: arrows left - 30

# for loop
for char in [wizard1, archer1]:  # Attacking with power of 60
  char.attack()  # Attacking with arrows: arrows left - 30

player_attack(user1)  # Do nothing


--------------


# when we keep both methods, from inheritance and local
class User:

  def sign_in(self):
    print('Logged in')

  def attack(self):  # initial attack function
    print('Do nothing')


class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):  # this attack function will override User attack
    User.attack(self)
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


player_attack(wizard1)  # Do nothing  // # Attacking with power of 60
player_attack(archer1)  # Attacking with arrows: arrows left - 30

# for loop
for char in [wizard1, archer1]:  # Do nothing  /  # Attacking with power of 60
  char.attack()  # Attacking with arrows: arrows left - 30

player_attack(user1)  # Do nothing




------------------------------------------------------------------------------



# super()
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)        # one way to pass argument
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)


----------

# super()
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)        # reffering to Super Class (class above), no self needed
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)

-------------


# introspection - the ability to determine the object at run time
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)        # reffering to Super Class (class above), no self needed
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(dir(wizard1))
