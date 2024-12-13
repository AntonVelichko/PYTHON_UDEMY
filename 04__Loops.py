
# 68 loops
for item in 'Zero':
  print(item)                     # 'z' 'e' 'r' 'o'

for item in (1,2,3):
  for x in ['a','b','c']:
    print(item, x)                # '1 a'  '1 b' ...



--------------------------------------------------------------------



# 69 iterables
# iterate -> one by one, check each item in a collection

user = {
  'name': 'Gollum',
  'age': 5006,
  'can_swim': False
}

for item in user:
  print(item)                       # name   age ...

for item in user.items():
  print(item)                       # ('name', 'Gollum') ...

for item in user.keys():
  print(item)                       # name  age ...

for item in user.values():
  print(item)                       # Gollum  5006 ...


for item in user.items():
  key, value = item
  print(key, value)                 # name Gollum   age 5006 ...

for key, value in user.items():     # can use 'k' and 'v'  / any variables 
  print(key, value)                 # name Gollum  age 5006 ...


# iterable items --> sets, lists, tuples, dictionaries, strings
--------------------------------------------------------------------



# 70 Simple compile
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for a in my_list:
  sum = sum + a
print(sum)                          # 55



# 71 range
for i in range(0, 10):
  print(i)                          # 0 1 2 ... 9

for _ in range(0, 10, 2):           # _ means that variable doesn't matter
  print('email')                    # email ... (x5)

for i in range(0, 10, 2):
  print(i)                          # 0  2  4  6  8

for _ in range(5, 0, -1):           # reversing range
  print(_)                          # 5 4 3 2 1

# https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
for x in reversed(whatever):
    do_something()


def reverse(text):
    result = ""
    for i in range(len(text),0,-1):
        result += text[i-1]
    return (result)
print(reverse('abcde'))         # edcba
# same can do --> text[::-1]
# same can do --> "".join(reversed(text))


for _ in range(3):
  print(list(range(10)))            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ... (x3)



# 72 enumerate()
for char in enumerate('abc'):
  print(char)                       # (0, 'a') (1, 'b') (2, 'c')

for i, char in enumerate('abc'):
  print(i, char)                    # 0 a  1 b  2 c
  
for i, char in enumerate(list(range(10))):
  if char == 5:
    print(f'index of 5 is: {i}')    # index of 5 is: 5



--------------------------------------------------------------------



# 73 while loop
i = 0
while i < 5:
  print(i)                    # 0
  break

i = 10
while i < 15:
  print(i)                    # 10 11 12 13 14
  i = i + 1

i = 20
while i < 25:
  print(i)                    # 20 21 22 23 24
  i = i + 1
else:
  print('done counting')      # done counting

i = 0
while i < 5:
  print(i)                    # 0
  i = i + 1
  break                       # 'break' stops the loop
else:
  print('done')



--------------------------------------------------------------------



# 74 loops
for item in [1,2,3]:          # more simple
  print(item)                 # 1 2 3

i = 0
while i < len([1,2,3]):       # more powerful
  print(i)                    # 0 1 2
  i += 1



--------------------------------------------------------------------



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



--------------------------------------------------------------------



# 75 break, continue, pass
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
  pass                      # just a temporary placeholder


--------------------------------------------------------------------



# 76 our first GUI
# Display the image below to the right hand side where the 0 is going to be ' ', 
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
    if (pixel == 1):
      print('*', end = '')
    else:
      print(' ', end = '')
  print('')                       # can use also print()


# clean 
# readability
# predictability
# do not repeat yourself (DRY)


fill = '$'
empty = ' '
for row in picture:
  for pixel in row:
    if (pixel):
      print(fill, end = '')
    else:
      print(empty, end = '')
  print('')


# my version
string = ''
for row in picture:
  for pixel in row:
    if (pixel):
      string = string + '#'
    else:
      string = string + ' '
  string = string  + '\n'
print(string)



--------------------------------------------------------------------



# 78 find duplicates
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dupl = []
for value in my_list:
  if my_list.count(value) > 1:
    if value not in dupl:
      dupl.append(value)
      
print(dupl)                           # ['b', 'n']

