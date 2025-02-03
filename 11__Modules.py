
..\Desktop\Python\module



# Built-In Modules
 https://docs.python.org/3/py-modindex.html

# Third Party Modules
https://pypi.org/
https://www.makeuseof.com/tag/install-pip-for-python/




##########################################################################################################################
###  sys.argv  ###
https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/





##########################################################################################################################


from collections import Counter, defaultdict, OrderedDict

###  Counter  ###
li = [1,2,3,4,5,5]							# Counter({5: 2, 1: 1, 2: 1, 3: 1, 4: 1})
print(Counter(li))

sentence = 'blah blah blah test'			# Counter({'b': 3, 'l': 3, 'a': 3, 'h': 3, ' ': 3, 't': 2, 'e': 1, 's': 1})
print(Counter(sentence))






###  defaultdict  ###
dict = {'a': 1, 'b': 2}
print(dict['a'])							# 1
# print(dict['c'])							# KeyError: 'c'

dict = defaultdict(int, {'a': 1, 'b': 2})
print(dict['c'])							# 0
print(int())								# 0  <-- that's why 'defaultdict' gives '0'

dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dict['c'])														# 5

dict = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dict['c'])														# does not exist





###  OrderedDict  ###
# dictionary that maintains the order
# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
# You can read more about it here:  https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d1 == d2)								# True


--------------


d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)								# False



# there is no order in a regular dictionary
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)								# True






###  datetime  ###
import datetime

print(datetime.time())					# 00:00:00
print(datetime.time(5,45,2))			# 05:45:02
print(datetime.date.today())			# 2025-01-30






###  array  ###
# array takes less memory and performs faster
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# https://docs.python.org/3/library/array.html

from array import array

arr = array('i', [1,2,3])
print(arr[0])							# 1






.
