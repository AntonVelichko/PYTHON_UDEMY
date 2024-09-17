#Pure Function
def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list
	
print(multiply_by2([1,2,3]))


-----


def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return print(new_list)  # this is not pure, has side effect
	
multiply_by2([1,2,3])


----


new_list = []  # this is not pure, has side effect
def multiply_by2(li):
	for item in li:
		new_list.append(item * 2)
	return new_list
	
new_list = []  # this is not pure, has side effect
	
multiply_by2([1,2,3])


---------------------------------------------------------------------------


# map, filter, zip, reduce
def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, [1,2,3])))	# [2, 4, 6]

---

my_list = [1,2,3]
def multiply_by2(item):
	return item * 2

print(list(map(multiply_by2, [1,2,3])))	# [2, 4, 6]
print(my_list)	# [1,2,3]

---

# filter
my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, [1,2,3])))	# [2, 4, 6]
print(my_list)	# [1,2,3]

---

# zip
my_list = [1,2,3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))	# [(1, 10), (2, 20), (3, 30)]

--

my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = ['a', 'b', 'c']

print(list(zip(my_list, your_list, their_list)))	# [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]

