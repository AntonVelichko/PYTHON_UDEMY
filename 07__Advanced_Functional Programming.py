

##########################################################################################################################
###  PURE FUNCTION  ###

# impossible to have Pure Functions everywhere
# functional programming separates Data and Functions when OOP combines Data and Functions



def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list
	
print(multiply_by2([1,2,3]))			# [2, 4, 6]



---------------



def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return print(new_list)  		# this is not pure and has a side effect like "print"
	
multiply_by2([1,2,3])				# [2, 4, 6]



---------------



new_list = []  					# this is not pure and has a side effect  -->  "new_list" is outside if the function scope
def multiply_by2(li):
	for item in li:
		new_list.append(item * 2)
	return new_list
	
new_list = []  					# this is not pure and has a side effect
	
multiply_by2([1,2,3])				# showes nothing






##########################################################################################################################
###  MAP  ###


def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list

print(list(map(multiply_by2, [1,2,3])))         # int' object is not iterable
                                                # because with "map" we don't need "list" anymore



def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, [1,2,3])))		# [2, 4, 6]



---------------



my_list = [1,2,3]
def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, my_list)))		# [2, 4, 6]
print(my_list)					# [1,2,3]






##########################################################################################################################
###  FILTER  ###


my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))	# [1, 3]
print(my_list)	# [1,2,3]






##########################################################################################################################
###  ZIP  ###


my_list = [1,2,3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))	# [(1, 10), (2, 20), (3, 30)]



---------------



my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = ('a', 'b', 'c')

print(list(zip(my_list, your_list, their_list)))	# [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]






##########################################################################################################################
###  REDUCE  ###


from functools import reduce
my_list = [1,2,3]

def accumulator(acc, item):
	print(acc, item)		# 0 1  \n  1 2  \n  3 3
	return acc + item

print(reduce(accumulator, my_list, 0))		# 6






*************************************************************************************************************************
***  EXERCISE  ***


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()	# OR return item.capitalize()

print(list(map(capitalize, my_pets)))					# ['SISI', 'BIBI', 'TITI', 'CARLA']



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))			# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]



#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))				# [73, 65, 76, 100, 88]



#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))			# 456






##########################################################################################################################
###  LAMBDA EXPRESSIONS  ###

# One time anonymous function
# Can be hard to read for others. Use carefully
# lambda param: action(param)


from functools import reduce

my_list = [1,2,3]

print(list(map(lambda item: item * 2, my_list)))            # [2, 4, 6]
print(list(filter(lambda item: item % 2 != 0, my_list)))    # [1, 3]
print(reduce(lambda acc, item: acc + item, my_list))        # 6
print(my_list)      # [1, 2, 3]






*************************************************************************************************************************
***  EXERCISE  ***


#Square
my_list = [5, 4, 3]
print(f'Squared list = {list(map(lambda item: item * item, my_list))}')            # [25, 16, 9]


# List Sorting by second number
arr = [(0, 2), (9, 9), (4, -2), (10, -1)]


### MY SOLUTION  ###
arr2 = []
for i in range(0, len(arr)): 
    min = arr[0][1]
    min_index = 0
    for item in arr:
        if(item[1] < min):
            min = item[1]
            min_index = arr.index(item)
    arr2.append(arr[min_index])
    arr.pop(min_index)


#print(f'Min = {min}')
#print(f'Min index = {min_index}')
print(arr2)              			# [(4, -2), (10, -1), (0, 2), (9, 9)]



---------------



###  TEACHER SOLUTION  ###
my_list = [5, 4, 3]

#Square
print(f'Squared list = {list(map(lambda item: item * item, my_list))}')            # [25, 16, 9]


# List Sorting by second number
arr = [(0, 2), (9, 9), (4, -2), (10, -1)]

arr.sort(key = lambda x: x[1])
print(arr)					# [(4, -2), (10, -1), (0, 2), (9, 9)]






##########################################################################################################################
###  COMPREHENSIONS  ###

# Quick way to create lists, sets, dicts instead of looping
# But can be confusing for others
# Maybe sometimes it is better not to use Comprehensions coz other programmers might not get it, and use just simple Descriptive Function


###  LIST  ##
# classic way to create list

my_list = []
for char in 'hello':
	my_list.append(char)

print(my_list)		# ['h', 'e', 'l', 'l', 'o']



---------------



# fast, easier way
[param for param in iterable]

my_list = [char for char in 'hello']
print(my_list)		# ['h', 'e', 'l', 'l', 'o']


my_list = [num for num in range (0,10)] 
print(my_list)         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_list = [num * 2 for num in range (0,10)] 
print(my_list)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


my_list = [num ** 2 for num in range(0,10) if num % 2 == 0]
print(my_list)      # [0, 4, 16, 36, 64]



---------------



###  SET  ###
my_list = {char for char in 'hello'}
print(my_list)		# {'h', 'o', 'l', 'e'}



---------------



###  DICTIONARY  ###
simple_dict = {
	'a' : 1,
	'b' : 2
}
my_dict = {key:value ** 2 for key, value in simple_dict.items()}		# can use any cariables {k:ve ** 2 for k, v in simple_dict.items()}
print(my_dict)          							# {'a': 1, 'b': 4}



simple_dict = {
	'a' : 1,
	'b' : 2
}
my_dict = {key + 'x':value ** 2 for key, value in simple_dict.items()}
print(my_dict)          							# {'ax': 1, 'bx': 4}



simple_dict = {
	'a' : 1,
	'b' : 2
}
my_dict = {key:value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)          							# {'b': 4}



my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)          							# {1: 2, 2: 4, 3: 6}






*************************************************************************************************************************
***  EXERCISE  ***


my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({item for item in my_list if my_list.count(item) > 1})
print(duplicates)               # ['b', 'n']


my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(list(set(filter(lambda item: my_list.count(item) > 1, my_list))))             # ['n', 'b']    ??? why starts with "n"



---------------



###  TEACHER SOLUTION  ###
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list( set([x for x in my_list if my_list.count(x) > 1]) )
print(duplicates)               # ['b', 'n']






