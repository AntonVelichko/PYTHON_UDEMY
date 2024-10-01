### GENERATORS

# range(100)
# list(range(100)

def make_list(num):
	result = []
	for i in range(num):		# range() is a generator
		result.append(i * 2)
	return result

my_list = make_list(100)		# my_list is point to location in the memory
print(my_list)


-------------------------------------------------------------------------------------------------------------------


# generators are iterable
# range is a generator
# list is iterable but not a generator

# general way to create a generator
# generators are usually functions

def generator_function():
	for i in range(10000):
		yield i		# that's the difference, no 'return'

---

def generator_function(num):
	for i in range(num):
		yield i		# yield pauses the functions and comes back when we do smth to it, which is called 'next'

for item in generator_function(100):
	print(item)

# only held one item in memory instead of having a whole list in memory



-------------------------------------------------------------------------------------------------------------------



def generator_function(num):
	for i in range(num):
		yield i

g = generator_function(100)	# instead of using a loop
next(g)
next(g)
print(next(g))               # 2
print(next(g))              # 3

# keep only the most recent data in memory, in this case it is '4'

-----

def generator_function(num):
	for i in range(num):
		yield i

g = generator_function(1)	# instead of using a loop
next(g)
print(next(g))               # StopIteration - when exeed the number of items



