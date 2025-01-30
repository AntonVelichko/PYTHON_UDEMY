
# Built-In Modules
 https://docs.python.org/3/py-modindex.html

# Third Party Modules
https://pypi.org/
https://www.makeuseof.com/tag/install-pip-for-python/




from collections import Counter, defaultdict, OrderedDict


li = [1,2,3,4,5,5]							# Counter({5: 2, 1: 1, 2: 1, 3: 1, 4: 1})
print(Counter(li))

sentence = 'blah blah blah test'			# Counter({'b': 3, 'l': 3, 'a': 3, 'h': 3, ' ': 3, 't': 2, 'e': 1, 's': 1})
print(Counter(sentence))




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




# dictionary that maintains the order
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d1 == d2)								# True



d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)								# False



# there is no order in regular dictionary
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)								# True
