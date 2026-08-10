# List in Python:

"""
List: A list allows you to store multiple values inside a single variable. They are mutable.
"""

# Syntax:

li = [415,5,78,12,37];
print(li);

# list can contain different datatypes:

li_ = ["ayush", 25, None, True, 50234.5];
print(li_, type(li_));

# Accessing List elemnts:
print(li[0])
print(li[1])
print(li[len(li)-1]) #bcz index starts from 0, also this is accessing last element of any list

# adding element
li.append(73000);
print(f"New List: {li}");

# insert at specific position:
li.insert(0, 96000);
print(f"New List Updated: {li}");

# extend: adds new object:

li_1 = [1,2,3];
li_2 = [4,5,6,7];

li_1.extend(li_2);
print(f"Extended List: {li_1}");

# remove: removes the first matching value:

li_1.remove(2);
print(f"removed li: {li_1}");

# pop: removes value by index

li_1.pop(4);
print(f"removed element: {li_1}");

# pop: without index: removes element from the last:
li_1.pop();
print(f"List: {li_1}");

# slicing list: list[start_index, stop_index]

numbers = [1,2,3,4,5,6,7,8,9,10];
print(f"sliced list: {numbers[1:4]}");

print(f"sliced list: {numbers[1:]}");
print(f"sliced list: {numbers[:3]}");
# slicing with step:
print(f"sliced list: {numbers[::2]}")
# reverse a list:
print(f"Reversed list: {numbers[::-1]}");
# search in array:
print(f"Search 3: {3 in numbers}");

# looping through list:

sales = [45000,780000,10000,50000,13000];

for sale in sales:
    print(sale);

# creating new list from available data:
high_sales = [];

for sale in sales:
    if sale>15000:
        high_sales.append(sale);

print(f"High sales data: {high_sales}");

# sort:
sales.sort()
print(sales);

sales.sort(reverse=True);
print(sales);

# sorted(): creates a new sorted list:

result = sorted(sales);
print(result);

# min(list), max(list), sum(list)

# list comprehension: a concise way of creating a new list from an exisiting one.

numbers = [10,5,3,8,1,4,45];

squares = [number**2 for number in numbers];
print(f"squared list: {squares}");

# list comprehension with conditionals:

even_list = [number for number in numbers
             if number%2==0];

print(f"even_list: {even_list}");

# 2-D list:

sales = [
    [10000,5000,21000],
    [4000,7000,55000],
    [75000,35000,78000]
]

# Reference behaviour:

sales = [1000,400,19000];
backup = sales;

backup.append(5000);
print(f"sales: {sales}\nbackup: {backup}");

"""
Why above happens:
sales  ──────┐
             ↓
        [100,200,300]
             ↑
backup ──────┘
bcz both sales and backup refer to same list object. to create shallow copy:
"""

backup_ = sales.copy();
backup_.append(2800);
print(f"sales: {sales}\nbackup: {backup_}");

# aliter:
backup__ = sales[:];
backup__.append(3500);
print(f"backup__: {backup__}");

