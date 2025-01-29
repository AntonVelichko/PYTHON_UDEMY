
##########################################################################################################################
###  FOR LOOP  ###
# looping in iterable things (dict, list, tuple, set, string)
# all these can be iterated

for item in 'Zero':
  print(item)                     # 'z' 'e' 'r' 'o'



for item in (1, 2, 3):
  for x in ['a', 'b', 'c']:
    print(item, x)                # '1 a'  '1 b' ...


for item in 50:
  print(item)                     # error: 'int' object is not iterable






##########################################################################################################################
###  ITERABLES  ###
# iterate -> one by one, check each item in a collection

user = {
  'name': 'Gollum',
  'age': 5006,
  'can_swim': False
}

for item in user:
  print(item)                       # name
                                    # age
                                    # can swim

for item in user.items():
  print(item)                       # ('name', 'Gollum')  
                                    # ('age', 5006)  ...
                                    # ...

for item in user.keys():
  print(item)                       # name  
                                    # age
                                    # ...

for item in user.values():
  print(item)                       # Gollum  
                                    # 5006
                                    # ...



for item in user.items():
  key, value = item
  print(key, value)                 # name Gollum   
                                    # age 5006
                                    # ...


for key, value in user.items():     # can use 'k' and 'v'  / any variables 
  print(key, value)                 # name Gollum
                                    # age 5006
                                    # ...






*************************************************************************************************************************
***  EXERCISE  ***

# simple counter
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for a in my_list:
  sum = sum + a
print(sum)                          # 55






##########################################################################################################################
###  RANGE  ###

print(range(100))                   # range(0, 100)  <<--  this is special type of object
print(range(0, 100))                # range(0, 100)


for i in range(0, 10):
  print(i)                          # 0
                                    # ...
                                    # 9

for _ in range(0, 10, 2):           # _ means that variable doesn't matter in this case, we just want to use 'range'
  print('email')                    # email ... (x5)



for i in range(0, 10, 2):
  print(i)                          # 0  2  4  6  8


  
for _ in range(5, 0, -1):           # reversing range
  print(_)                          # 5 4 3 2 1



for _ in range(3):
  print(list(range(10)))            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
for x in reversed(whatever):
    do_something()

# All of these three solutions give the same results if the input is a string:
# 1
def reverse(text):
    result = ""
    for i in range(len(text),0,-1):
        result += text[i-1]
    return (result)
print(reverse('abcde'))         # edcba

# 2
text[::-1]

# 3
"".join(reversed(text))






##########################################################################################################################
###  ENUMERATE  ###

for char in enumerate('abc'):
  print(char)                           # (0, 'a')
                                        # (1, 'b')
                                        # (2, 'c')


for i, char in enumerate('abc'):
  print(i, char)                        # 0 a 
                                        # 1 b
                                        # 2 c


for i, char in enumerate ((1,2,3)):
  print(i, char)                        # 0 1
                                        # 1 2
                                        # 2 3


# find index of specific item
for i, char in enumerate(list(range(10))):
  if char == 5:
    print(f'index of 5 is: {i}')        # index of 5 is: 5






##########################################################################################################################
###  WHILE LOOP  ###

i = 0
while i < 5:
  print(i)                    # 0
  break



i = 10
while i < 15:
  print(i)                    # 10
  i = i + 1                   # 11
                              # ...
                              # 14


i = 20
while i < 25:
  print(i)                    # 20 / 21 / 22 / 23 / 24
  i = i + 1
else:                         <<-- 'else' executing only when 'while' loop is finished
  print('done counting')      # done counting



i = 0
while i < 5:
  print(i)                    # 0
  i = i + 1
  break                       # 'break' stops the loop, 'else' statement doesn't execute
else:
  print('done')






##########################################################################################################################
###  FOR or WHILE  ###

for item in [1,2,3]:          # more simple
  print(item)                 # 1 2 3



i = 0
while i < len([1,2,3]):       # more powerful; use when you don't know how many times to loop
  print(i)                    # 0 1 2
  i += 1






##########################################################################################################################
###  WHILE TRUE  ###
while True:
  print('something')                      # something
  break


while True:
  input('say something: ')                # say something: ___
  break


while True:
  response = input('say \'bye\': ')       # say bye: ___
  if (response == 'bye'):
    print('Bye to you!')                  # Bye to you!
    break






##########################################################################################################################
###  BREAK, CONTINUE, PASS  ###

my_list = [1,2,3]
for item in my_list:
  print(item)               # 1
  break



my_list = [10,20,30]
for item in my_list:
  print(item)               # 10 20 30
  continue



my_list = [7,8,9]
for item in my_list:
  continue
  print(item)               # nothing happens



my_list = [7,8,9]
i = 0
while i < len(my_list):cx
for item in my_list:
  # thinking about it
  pass                      # just a temporary placeholder, not very useful







*************************************************************************************************************************
***  EXERCISE  ***

# first GUI
# Display the image below to the right-hand side where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if (pixel):
      print('*', end = '')
    else:
      print(' ', end = '')
  print('')                       # can use also print()






##########################################################################################################################
###  CLEAN CODE  ###

# clean 
# readability (don't need to be very smart to use some techniques)
# predictability
# do not repeat yourself (DRY)
# keep code reusable


fill = '$'
empty = ' '
for row in picture:
  for pixel in row:
    if pixel:
      print(fill, end = '')
    else:
      print(empty, end = '')
  print('')



###  MY VERSION  ###
string = ''
for row in picture:
  for pixel in row:
    if pixel:
      string = string + '#'
    else:
      string = string + ' '
  string = string  + '\n'
print(string)






*************************************************************************************************************************
***  EXERCISE  ***
# find duplicates

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dupl = []
for value in my_list:
  if my_list.count(value) > 1:
    if value not in dupl:
      dupl.append(value)
      
print(dupl)                           # ['b', 'n']






.
