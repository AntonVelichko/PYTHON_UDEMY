
##########################################################################################################################
### DICTIONARY  ###

# dict is a data type and data structure
# unordered data (key-value pair), list is ordered data
# ordered dict - https://medium.com/junior-dev/python-dictionaries-are-ordered-now-but-how-and-why-5d5a40ee327f


dictionary = {
  'a': 1,                   # key, value
  'b': 2,
  'c': [1,2,3],
  'd': 'hello',
  'e': True,
  1: 'x',
  (1,2): [1,2,3]
}

print(dictionary['b'])      # 2
print(dictionary[(1,2)])    # [1, 2, 3]
print(dictionary['x'])      # gives Error



--------------



arr = [
  {
    'a': [1,2,3],
    'b': 'hi'
  },
  {
    'a': [4,5,6],
    'b': False
  }
]
print(arr[0]['a'][1])       # 2






##########################################################################################################################
### DICTIONARY KEYS  ###

# keys need to be immutable
# keys have to be unique or will be overwritten
# keys should be descriptive, 99% it will be a string

dictionary = {
  'a': 1,
  123: [1,2,3],
  True: 'Yes',
  [100]: True                # mutable, gives error
}





##########################################################################################################################
### DICTIONARY METHODS  ###
# https://www.w3schools.com/python/python_ref_dictionary.asp


dictionary = {
  'a': 1,
  'b': 2
}




# adding
dictionary['New'] = 'Sample'
print(dictionary)               # {'a': 1, 'b': 2, 'New': 'Sample'}




# .get()
print(dictionary.get('a'))                                # 1
print(dictionary.get('age'))                              # None

# return the value of an item that does not exist
# means grab the 'c' from the dictionary; if it doesn't exist, then use '3' by default
print(dictionary.get('c', 3))                             # 3

# if the key exists, it doesn't overwrite the value
print(dictionary.get('a', 10))                            # 1
print(dictionary)                                         # {'a': 1, 'b': 2}




# another way to create a dictionary, but not very common
dictionary_2 = dict(name = 'John', age = 55)
print(dictionary_2)                                       # {'name': 'John', 'age': 55}




# IN keys
dictionary = {
  'a': 1,
  'b': 2
}

# keys, value
print('a' in dictionary)              # True
print('a' in dictionary.keys())       # True
print(1 in dictionary)                # False
print(1 in dictionary.values())       # True


# items
print(dictionary.items())             # dict_items([('a', 1), ('b', 2)])
print(('a',1) in dictionary.items())  # True
print('a' in dictionary.items())      # False
print(1 in dictionary.items())        # False


# .copy()   /returns a copy of dict
dict_2 = dictionary.copy()
print(dict_2)                         # {'a': 1, 'b': 2}


# .pop()   /removes key and value, returns value
print(dictionary.pop('a'))            # 1
print(dictionary)                     # {'b': 2}


# .update()   /returns none
print(dictionary.update({'b': 12}))   # None
print(dictionary)                     # {'b': 12}


# .update()   /can add a new item
dictionary.update({'a': 11})
print(dictionary)                     # {'b': 12, 'a': 11}
# if key doesn't exist, it will still update with the key item


# clear (returns None)
dictionary.clear()
print(dictionary)                     # {}

# or clear with {}
dictionary = {}
print(dictionary)                     # {}


# .popitem() 
# /removes the last one since Python 3.7, before dict was unordered so basically, it removed some random item
# useful to destructively iterate over a dictionary






*************************************************************************************************************************
***  EXERCISE  ***

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
  'age': 23,
  'username': 'Tommy',
  'weapons': ['sword'],
  'is_active': True,
  'clan': 'Aphalachi'
}
print(user)


#2 iterate and print all the keys in the above user.
print(user.keys())         # dict_keys(['age', 'username', 'weapons', 'is_active', 'clan'])
print(user.values())       # dict_values([23, 'Tommy', ['sword'], True, 'Aphalachi'])


#3 Add a new weapon to your user
user['weapons'].append('shield')
print(user)


#4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})
print(user)


#5 Ban the user by setting the previous key to True
user['is_banned'] = True          # user.update({'is_banned': True})
print(user)


#6 create a new user2 by copying the previous user and updating the age and username values. 
user2 = user.copy()
user2.update({'age': 35, 'username': 'Jimmy'})
print(user2)






### TEACHER SOLUTION  ###

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}


# 2 iterate and print all the keys in the above user.
print(user_profile.keys())


# 3 Add a new weapon to your user
user_profile['weapons'] = 'Katana'


# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})


# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True


# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user_profile)
print(user2)






-
