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


---


