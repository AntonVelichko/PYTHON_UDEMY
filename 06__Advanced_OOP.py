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
print(type({}))                      # <class 'dict'>
print(type(obj1))                    # <class '__main__.BigObject'>


----------------------------------------------------------------------


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
help(list)                        # to see the lass List blueprint





----------------------------------------------------------------------


class PlayerCharacter:
    membership = True                    # if False --> AttributeError: 'PlayerCharacter' object has no attribute 'name'
    def __init__(self, name, age):
        if(self.membership):             # self refers to this PlayerCharacter
            self.name = name
            self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 20)
player2.attack = 50

print(player1.name)     # Cindy
print(player1.run())    # run
                        # None


----------------------------------------------------------------------


class PlayerCharacter:
    membership = False                                      # if False --> AttributeError: 'PlayerCharacter' object has no attribute 'name'
    def __init__(self, name = 'anonymous', age = 20):       # by default
        if(age >= 18 and self.membership):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

player1 = PlayerCharacter('Tom', 18)
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
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 10)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.adding_things(2,3))                    # 5
print(player2.name, player2.age)                    # anonymous 20
print(PlayerCharacter.adding_things(3,4))            # 7






class PlayerCharacter:
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


print(PlayerCharacter.adding_things(3,3))    # <__main__.PlayerCharacter object at 0x72fbc215bee0>
                                             # object 'Teddy' instantiated with age = num1 + num2
player = PlayerCharacter.adding_things(11,11)
print(player.age)                            # 22
print(player.name)                           # Teddy





class PlayerCharacter:
    membership = True
    def __init__(self, name = 'anonymous', age = 20):
        if(age >= 18):
            self.name = name
            self.age = age

    def run(self):
        print('Run')

    @classmethod            # method for the actual class, not used often (5%)
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player = PlayerCharacter.adding_things(11,11)
print(player.age)                            # 22
print(player.name)                          # Teddy



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

de = DecoratorExample()                     # Hello, World!

de.example_function()                       #I'm a decorated function!
print('---')

DecoratorExample().example_function()       # Hello, World!
print('---')                                # I'm a decorated function!

DecoratorExample.example_function()         # I'm a decorated function!
print('----')




# Instance Methods
class DecoratorExample:
  # Example Class """
  def __init__(self):
    # Example Setup """
    print('Hello, World!')
    self.name = 'Decorator Example'

  def example_function(self):
    # This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)

de = DecoratorExample()     # Hello, World!
de.example_function()       # I'm an instance method!
                            # My name is Decorator Example




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

de = DecoratorExample.example_function()    # I'm a static method!





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

de = DecoratorExample()         # Hello, World!
de.example_function()           # I'm a class method!
                                # Hello!






# Incapsulation
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




# if there are no methods - it's useless
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('Tony', 99)
print(player1.name)         # Tony
print(player1.age)          # 99

player2 = {'name': 'John', 'age': 100}
print(player2['name'])      # John
print(player2['age'])       # 100
# the difference between player1 and player2 is the access to information





# Absraction

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('Tony', 99)
player1.name = '!!!'
player1.speak = 'Booo'

print(player1.speak)    # Booo
print(player1.name)     # !!!
print(player1.speak())  # TypeError: 'str' object is not callable







# Inheritance

class User:
  def sign_in (self):      # if no attributes then we don't need __init__ , we do not initialize anything
    print('Logged in')

class Wizard(User):        # 'class Wizard' INHERITS methods from 'class User'
  pass

class Archer(User):
  pass

wizard1 = Wizard()
wizard1.sign_in()       # Logged in



--------------------------------------------------


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



-----------------------------------------------------------------------------------------------------------


###   _var - means this variable is PRIVATE; do not change it   ###


-----------------------------------------------------------------------------------------------------------


###  POLYMORPHISM  ###

class User:
  def sign_in(self):
    print('Logged in')

  def attack(self):              # initial attack function
    print('Do nothing')


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):              # this attack function will override User attack
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


player_attack(wizard1)              # Attacking with power of 60  -->  using 'def player_attack(char):'
wizard1.attack()                    # Attacking with power of 60  -->  using 'class Wizard(User):'
Wizard('Saruman', 70).attack()      # Attacking with power of 70
player_attack(archer1)              # Attacking with arrows; arrows left - 30


# for loop
for char in [wizard1, archer1]:      # Attacking with power of 60
  char.attack()                      # Attacking with arrows: arrows left - 30

player_attack(user1)    # Do nothing
user1.attack()          # Do nothing


--------------


# when we keep both methods, from inheritance and local
class User:
  def sign_in(self):
    print('Logged in')

  def attack(self):                  # initial attack function
    print('Do nothing')


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


player_attack(wizard1)  # Do nothing
                        # Attacking with power of 60
wizard1.attack()        # Do nothing
                        # Attacking with power of 60
player_attack(archer1)  # Attacking with arrows: arrows left - 30


# for loop
for char in [wizard1, archer1]:      # Do nothing  \n  # Attacking with power of 60
  char.attack()                      # Attacking with arrows: arrows left - 30

player_attack(user1)                  # Do nothing




-----------------------------------------------------------------------------------------------------------


###  SUPER CLASS  ###

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):      # this shows the ORDER of arguments
        User.__init__(self, email)               # one way to pass argument
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
        super().__init__(email)                # reffering to Super Class (class above), no self needed
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)        # merlin@gmail.com



-------------



# Exercise Extending List

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
print(len(super_list1))                 # 1000

super_list1.append(5)                   
print(super_list1[0])                   # 5
print(issubclass(SuperList, list))      # True
print(issubclass(list, object))         # True




-----------------------------------------------------------------------------------------------------------


###  INTROSPECTION - the ability to determine the object at run time  ###

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
print(dir(wizard1))    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',  ...  'attack', 'email', 'name', 'power', 'sign_in']




##########################################################################################################################
###  DUNDER METHODS  ###
https://docs.python.org/3/reference/datamodel.html#special-method-names

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
action_figure = Toy('red', 0)

print(action_figure.__str__())  # <__main__.Toy object at 0x773cad9efc90>
print(str(action_figure))       # <__main__.Toy object at 0x773cad9efc90>


-----


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        
    def __str__(self):
        return f'{self.color}'
        
action_figure = Toy('red', 0)
print(action_figure.__str__())      # red  |  'str' is modified only when used with a specific object ('Toy' in our case)
print(str(action_figure))           # red
print(str('action_figure'))         # action_figure
print(str(123) + 'a')               # 123a
print(type(str(123)))               #  <class 'str'>


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




##########################################################################################################################
###  MULTIPLE INHERITANCE  ###
Complicates code; be very cautious. Maybe avoid it to use

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
        print('Run fast Wazard')


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

print(hb1.run())    # Run fast Wizard  \n  None    | Order matters; if Archer first in 'class HybridBorg(Archer, Wizard)' it will gives 'Run fast Archer'
print(hb1.name)     # orgie
print(hb1.power)    # 50
print(hb1.arrows)   # showes nothing
print(hb1.check_arrows())   # gives an error since it doesn't know the arrows



-----------



# Miltiple Inheritance
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

print(hb1.run())            # Run fast Archer 
                            # None
print(hb1.check_arrows())   # 100 remaining  
                            # None
print(hb1.attack())         # Attacking with power of 50 
                            # Order matters; 'def __init__(self, name, power, arrows):'
                            # in this case, it will be Wizard
                            # None
print(hb1.sign_in())        # Logged in  
                            # None



##########################################################################################################################
###  MRO  ###
__mro__
http://www.srikanthtechnologies.com/blog/python/mro.aspx
This will be a bad code since it's complicated to understand

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)    # (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)


'''
    object
 ↑     ↑    ↑
 X     Y     Z
  ↖ ↗    ↖ ↗
   A      B
      ↖ ↗
       M
'''



-----------------------------------------------------------------------------



# Exercise

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

#OR my_cats = [Simon('Simon', 1), Sally('Sally', 2), Bob('Bob', 3)]


#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)


#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

print(cat1.sing('Moew'))        # Moew



