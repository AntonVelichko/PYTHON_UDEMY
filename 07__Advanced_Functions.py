#Pure Function
def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list
	
print(multiply_by2([1,2,3]))		# [2, 4, 6]


-----


def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return print(new_list)  # this is not pure and has a side effect
	
multiply_by2([1,2,3])		# [2, 4, 6]


----


new_list = []  # this is not pure and has a side effect
def multiply_by2(li):
	for item in li:
		new_list.append(item * 2)
	return new_list
	
new_list = []  # this is not pure and has a side effect
	
multiply_by2([1,2,3])		#


---------------------------------------------------------------------------


### map
def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, [1,2,3])))		# [2, 4, 6]

---

my_list = [1,2,3]
def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, my_list)))	# [2, 4, 6]
print(my_list)	# [1,2,3]


----------------------------------------


# filter
my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))	# [1, 3]
print(my_list)	# [1,2,3]


----------------------------------------


# zip
my_list = [1,2,3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))	# [(1, 10), (2, 20), (3, 30)]

---

my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = ['a', 'b', 'c']

print(list(zip(my_list, your_list, their_list)))	# [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]



----------------------------------------


# reduce
from functools import reduce
my_list = [1,2,3]

def accumulator(acc, item):
	print(acc, item)		# 0 1
					# 1 2
					# 3 3
	return acc + item

print(reduce(accumulator, my_list, 0))		# 6



----------------------------------------



### EXERCISE
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()	# OR return item.capitalize()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))






