# Tuples in Python:

"""
Tuples in Python

We've learned that a list is an ordered, mutable collection.

Now we'll learn about tuples.

A tuple is also an ordered collection, but the key difference is:

A tuple is immutable — once created, its elements cannot be changed.

Tuples are useful when you have a collection of values that should remain fixed.
"""

# syntax:
tup_1 = (10,20,30,40,50);
print(tup_1);

# tuple can also be created w/o parentheses:
tup_2 = 10,20,30;
print(tup_2);

"""
List V/S Tuple
| Feature                       | List                 | Tuple                           |
| ----------------------------- | -------------------- | ------------------------------- |
| Ordered                       | ✅                    | ✅                               |
| Indexed                       | ✅                    | ✅                               |
| Allows duplicates             | ✅                    | ✅                               |
| Mutable                       | ✅                    | ❌                               |
| Syntax                        | `[]`                 | `()`                            |
| Can be used as dictionary key | ❌                    | ✅, if all elements are hashable |
| Typical use                   | Data that may change | Fixed/grouped data              |

"""

# Access tuple elements:
sales = (10,20,457,733,343);
print(sales[0])
print(sales[1])
print(sales[2]);

# sales[0] = 75000; error: TypeError

# Slicing:
print(sales[0:2]);
print(sales[:]);

"""
Why Would We Want Immutability?
At first you might think:
"Why not just use lists for everything?"
Because sometimes you want to guarantee that data cannot accidentally change.
"""

# single element tuple:

tup_3 = (10,); #always need a comma, else python interprets it as an integer.

# tuple packing: 
employee = "EMP001", "Ayush Dutta", 25; #python automatically packs this into a tuple
print(employee); 

# tuple unpacking:
employee_id, name, age = employee;
print(employee_id, name, age);

# returning multiple values from a fn:
def calc(a,b):
    total = a+b;
    difference = a-b;
    return total, difference;#this will return a tuple: tuple packing

print(calc(10,7));

# looping through a tuple:
for sale in sales:
    print(sale);

# Membership testing:
print(457 in sales);

# Tuple Methods:

# count
print(sales.count(733));

# index: finds the index of first occurence
print(sales.index(457));

# builtin fn:
print(len(sales));
print(min(sales));
print(max(sales));
print(sum(sales));

# tuples with different datatypoes

tup_4 = (10,"ayush", True,45.7, None);
print(tup_4);

# 2-D tuple:
regional_sales = (
    (45,758,964),
    (1,98,45),
    (45,75,84)
)

print(regional_sales[0][1]);

# list and tuples:

employees = [
    ("ayush", 25, "EMP001"),
    ("rohan", 26, "EMP002"),
    ("harry", 27, "EMP003"),
];

print(employees);

# swapping variable
a=10;
b=20;

a,b = b,a;# python first packs a and b into b, a and then unpacks again into a,b.

# extended unpacking:

numbers = (10,20,30,40,50);

first, *middle, last = numbers;
print(first, middle, last);

