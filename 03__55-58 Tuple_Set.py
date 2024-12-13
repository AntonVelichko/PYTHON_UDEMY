
# 55 Tuple
# immutable list (can't be sorted)
tuple_1 = (1,2,3,4,5)
#tuple_1[0] = 10                    # Error
print(tuple_1[0])                   # 1

# in
print(5 in tuple_1)                 # True

dict_1 = {
  'a': 1,
  'b': 2
}

# items return tuple
print(dict_1.items())               # dict_items([('a', 1), ('b', 2)])



----------------------------------------------------------------------------------



#56 Tuple Methods
# https://www.w3schools.com/python/python_ref_tuple.asp
tuple_1 = (1,2,3,4,5)

# copy
tuple_2 = tuple_1[1:2]
print(tuple_2)              # (2,)   /if it's a single item, then will be a comma at the end
print(tuple_1)              # (1, 2, 3, 4, 5)

tuple_3 = tuple_1[1:4]
print(tuple_3)              # (2, 3, 4)

x,y,z, *other = (1,2,3,4,5)
print(x)                    # 1
print(other)                # [4, 5]

# .count   /how many times does item appear in tuple
tuple_1 = (1,2,3,4,5,2)
print(tuple_1.count(2))     # 2

# .index()   /shows the first index of the item if there are more than one similar item
print(tuple_1.index(5))     # 4
print(tuple_1.index(2))     # 1

# len
print(len(tuple_1))         # 6



------------------------------------------



# 57 Sets
# unordered collection of unique subjects
set_1 = {1,2,3,4,5}
print(set_1)                                      # {1, 2, 3, 4, 5}

set_2 = {1,2,3,4,5,5}
print(set_2)                                      # {1, 2, 3, 4, 5}

# .add()
set_2.add(6)
set_2.add(2)
print(set_2)                                      # {1, 2, 3, 4, 5, 6}

# set()   /convert list to set
list_1 = [1,2,3,4,5,5,4]
print(set(list_1))                                # {1, 2, 3, 4, 5}

# set like dictionary can't be addressed by index, only by value
print(1 in set_2)                                 # True
#print(set_2[1])                                  # Error
#print(set_2[0])                                  # Error

# len()   /count only unique values
set_3 = {1,2,3,3,2,1}
print(len(set_3))                                 # 3

# list()   /convert set to list
print(list(set_3))                                # [1,2,3]

# .copy()
set_4 = set_3.copy()
set_4.add('a')
print(set_4)                                      # {1, 2, 3, 'a'}
print(set_3)                                      # {1, 2, 3}

# .clear()
set_4.clear()
print(set_4)                                      # set()



------------------------------------------



# 58 Set Methods
# https://www.w3schools.com/python/python_ref_set.asp
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}

# .difference()   / find difference / returns difference
set_1 = {1,2,3,4,5}
print(set_1.difference(set_2))                          # {1,2,3}
print(set_2.difference(set_1))                          # {6, 7, 8, 9, 10}
print(set_1)                                            # {1, 2, 3, 4, 5}

# .discard()   /delete item / returns None
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}
set_1.discard(5)
print(set_1)                                            # {1, 2, 3, 4}

# .difference_update()   /returns None
# removes all elements of another set from this set
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}
set_1.difference_update(set_2)
print(set_1)                                            # {1,2,3}

# .intersection()
set_1 = {1,2,3}
print(set_1.intersection(set_2))                        # set()   /if no intersection
print(set_1)                                            # {1,2,3}

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.intersection(set_2))                        # {4,5}
print(set_1)                                            # {1,2,3,4,5}

set_1 = {9,10,11}
set_2 = {4,5,6,7,8,9,10}
print(set_1.intersection(set_2))                        # {9,10}
print(set_1 & set_2)                                    # {9, 10}
print(set_1)                                            # {9,10,11}

# .isdisjoint()   /if it hasn't common values
set_1 = {1,2,3}
set_2 = {4,5,6,7,8,9,10}
print(set_1.isdisjoint(set_2))                          # True

# .union()
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.union(set_2))                               # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set_1 = {3,4,5}
print(set_1 | set_2)                                    # {3, 4, 5, 6, 7, 8, 9, 10}

# .issubset()   / returns whether another set contains this set or not
set_1 = {4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.issubset(set_2))                            # True

set_1 = {3,4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.issubset(set_2))                            # False

# .issuperset()   / returns whether this set contains another set or not
set_1 = {4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.issuperset(set_2))                          # False
print(set_2.issuperset(set_1))                          # True

set_1 = {3,4,5}
print(set_1.issuperset(set_2))                          # False
print(set_2.issuperset(set_1))                          # False



------------------------------------------



# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal 
#can use to immediately find out who missed class so they can call the parents. 
#(Imagine if the list had 1000s of students. The principal can use the lists generated by 
#the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

print(school.difference(attendance_list))    # we don't have to convert the attendance_list to a set...it does it for you
