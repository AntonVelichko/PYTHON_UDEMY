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
