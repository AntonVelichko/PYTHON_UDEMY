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



-------------------------------------------------------------------------------------------------------------------


#generators.
#generators are much more performant than lists. (i.e range > list in performance.)
#So generators are really, really useful when calculating large sets of data.

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000000): #it finishes after.
        i*5

long_time()
print()

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)): #it took longer.
        i*5

long_time2()
print()


-------------------------------------------------------------------------------------------------------------------

### UNDER HOOD OF GENERATORS

# for - underneath the hood
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break


# range - underneath the hood
class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,100)
for i in gen:
    print(i)


