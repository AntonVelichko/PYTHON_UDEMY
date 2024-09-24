

# 41 Lists
arr = [1,2,'a', True]
print(arr[0])           # 1



----------------------------------------------------------------------------------



# 42 List Slicing
arr = [
  'a',
  'b',
  'c',
  'd'
]
print(arr[0:2])     # ['a', 'b']
print(arr[0::2])    # ['a', 'c']

arr[0] = 'x'
print(arr)          # ['x', 'b', 'c', 'd']

arr_2 = arr[:3]     #copy of arr from 0 to 3 indexes
arr_2[0] = 'y'

print(arr)          # ['x', 'b', 'c', 'd']
print(arr_2)        # ['y', 'b', 'c']

arr_3 = arr         # not a copy, just reference to data
arr_3[0] = 'w'
print(arr)          # ['w', 'b', 'c', 'd']
print(arr_3)        # ['w', 'b', 'c', 'd']

# list slicing creates new copy
arr_4 = arr[:]
arr_4[0] = 'n'
print(arr_4)        # ['n', 'b', 'c', 'd']
print(arr)          # ['w', 'b', 'c', 'd']

arr_5 = arr + ['t']
print(arr_5)        # ['w', 'b', 'c', 'd', 't']
print(arr)          # ['w', 'b', 'c', 'd']


----------------------------------------------------------------------------------



# 43 Matrix
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[0][1])     # 2



----------------------------------------------------------------------------------



# 44 List Methods
# https://www.w3schools.com/python/python_ref_list.asp
arr = [1,2,3,4,5]
print(len(arr))           # 5

# ADDING
# .append()   /returns None
arr.append(6)
print(arr)                # [1, 2, 3, 4, 5, 6]

ex = arr.append(7)
print(ex)                 # None
print(arr)                # [1, 2, 3, 4, 5, 6, 7]

# .insert()   /index, value   /returns None
arr.insert(1, 'x')        # index, value
print(arr)                # [1, 'x', 2, 3, 4, 5, 6, 7]

# .extend()   /returns None   /can add several values in the end
#                             / can add another list
arr.extend([8,9])
print(arr)                # [1, 'x', 2, 3, 4, 5, 6, 7, 8, 9]

# REMOVING
# .pop()   /returns deleted value
arr.pop()                 # delete last one
print(arr)                # [1, 'x', 2, 3, 4, 5, 6, 7, 8]

arr.pop(2)                # delete index
print(arr)                # [1, 'x', 3, 4, 5, 6, 7, 8]

# .remove()   /returns None
arr.remove('x')           # remove the first value
print(arr)                # [1, 3, 4, 5, 6, 7, 8]

# .clear()   /returns None
arr.clear()               # remove all
print(arr)                # []



----------------------------------------------------------------------------------



# 45 List Methods 2
# .index()   /returns the first index of value
arr = ['a','b','c','d','e','a']
print(arr.index('b'))             # 1
print(arr.index('d', 0, 4))       # 3 /starts from 0 and stops before 4 
print(arr.index('d', 0, 3))       # gives an error, in that range no 'd'

# keyword https://www.w3schools.com/python/python_ref_keywords.asp
# in
print('d' in arr)                 # True
print('x' in arr)                 # False

print('i' in 'hi')                # True

# .count()   / returns number
print(arr.count('a'))             # 2



----------------------------------------------------------------------------------



# 46 List Methods 3
arr = ['a','b','c','d','e','a']

# .sort()   /returns None
arr.sort()
print(arr)                          # ['a', 'a', 'b', 'c', 'd', 'e']

# sorted()   /returns new array
arr = ['a','b','c','d','e','a']
print(sorted(arr))                  # ['a', 'a', 'b', 'c', 'd', 'e']
print(arr)                          # ['a', 'b', 'c', 'd', 'e', 'a']

# .copy()   /returns new copy of array
arr_2 = arr.copy()                  # arr_2 = arr[:]
arr_2.sort()
print(arr_2)                        # ['a', 'a', 'b', 'c', 'd', 'e']

# .reverse()   /returns None
arr = ['a','b','c','d','e']
arr.reverse()
print(arr)                          # ['e', 'd', 'c', 'b', 'a']



----------------------------------------------------------------------------------



# 47 List Patterns
arr = ['a','b','c','d','e']

# len()
print(len(arr))                     # 5

# reverse by slicing (creates new list)
print(arr[::-1])                    # ['e', 'd', 'c', 'b', 'a']
print(arr)                          # ['a', 'b', 'c', 'd', 'e']

# copy by slicing (creates new list)
arr_2 = arr[:]
arr_2.reverse()
print(arr_2)                      # ['e', 'd', 'c', 'b', 'a']
print(arr)                        # ['a', 'b', 'c', 'd', 'e']

arr_3 = arr[0:1]
print(arr_3)                      # ['a']

arr_4 = arr[0:5:2]
print(arr_4)                      # ['a', 'c', 'e']

# range()   /generate a new list
print(list(range(1,10)))          # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# .join()   / last value is skipped
print(' '.join(['I','am','Jojo']))  # I am Jojo
print(' '.join('hello'))          # h e l l o
print('.'.join('PM'))             # P.M



----------------------------------------------------------------------------------



# 48 List Unpacking
a,b,c = [1,2,3]
print(a)                        # 1
print(b)                        # 2
print(c)                        # 3

a,b,c = 1,2,3
print(a)
print(b)
print(c)

a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)                          # 1
print(b)                          # 2
print(other)                      # [4, 5, 6, 7, 8, 9]

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)                          # 1
print(other)                      # [4, 5, 6, 7, 8]
print(d)                          # 9

