# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:43:23 2020

@author: Sourav Singh
"""

# List and its default functions
#A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements
list=(9,10,"ssr")
print(list)
# methods
#append (x)
a=["I","am"]
print(a)
a.append("ssr")
print(a)
#extend
a.extend(["the","ssr"])
print(a)
# insert
a.insert(4,"only")
print(a)
#remove
a.remove("ssr")
print(a)
# clear
a.clear()
print(a)
#count
print(a.count("i"))
# reserveb
b=[1,2,3,4,5,6,7]
b.reverse()
print(b)


# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)
# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)
# Q4

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])


# Q 5
#caitalize
z=("hello, my name is ssr")
print(z)
z=str.capitalize(z)
print(z)
#center
string = "Python is awesome"

new_string = string.center(24, '*')

print("Centered String: ", new_string)

text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)