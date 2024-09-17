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
