#variable in python

"""
What is a Variable?

A variable is a name that refers to a value stored in memory.

Think of your computer's memory (RAM) as a huge warehouse with millions of storage boxes.

When you write:

age = 25

Python performs these steps:

Creates the integer object 25.
Stores it somewhere in memory.
Creates the name age.
Makes age refer to that object.
"""

name = "Ayush Dutta";
print(f"Name: {name}, reference: {id(name)}")

'''
rules for nameing variable: read from ai
'''

# swap var

# 1.
a= 5;
b=7;
print(f"a: {a}, b: {b}")
temp = a;
a = b;
b = temp;
print(f"a: {a}, b: {b}");

# use type() to check datatype
name_ = "ayush"
age = 28;
job = "Network Engineer";
print(f"{type(name_)}, {type(age)}, {type(job)}");

# use id() for finding memory address
print(f"{id(name_)}")

# swap w/o temp var:
p = 5;
q = 7;
print(f"p: {p}, q: {q}")
p,q = q,p;
print(f"p: {p}, q: {q}");
