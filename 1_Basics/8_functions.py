# Functions in python:

"""
fn is a set of reusable code. fn can perform a task or return a value.
"""

# syntax of creating fn:

def function_name():
    # code
    ...


name = input("Enter your name: ");
def greet():
    print(f"Greetings, {name}!");

greet(); #invoking/calling fn

"""
Fn execution flow:

Define Function
      ↓
Store Function
      ↓
Continue Program
      ↓
Function Called
      ↓
Execute Function Body
"""

# fn with parameter:

def greet(name):
    print(f"Hello, {name}");

greet("Ayush");

"""
Parameter vs Argument

In simple terms:
Parameter = placeholder inside the function definition.
Argument = actual value passed to the function.
"""

# multi parameter

def calculate_total(price,quantity):
    total = price * quantity;
    return total;

p1= 10000;
q1 = 5;
print(f"Total is {calculate_total(p1, q1)}");

"""
Print v/s Return:
Use print() when you want to display something.
Use "return" when you want the function to produce a value that the rest of your program can use.
"""

# return multiple values:

def calculate(a,b):
    total = a+b;
    difference = a-b;
    return total, difference;

print(f"sum and difference are respectively: {calculate(10,3)}");

# default argument:

def greet(name, message="Welcome"):
    print(f"{name}, {message}");

greet("ayush");

# Keyword argument:

def employee(name, job):
    print(f"Employee Name: {name}\nJob: {job}");

employee(job="Embedded Systems Engineer", name="Ayush Dutta");

# variable length argument

def calculate_total(*numbers): #*numbers create a tuple
    total = 0
    for number in numbers:
        total+= number;

    return total;

print(f"Sum: {calculate_total(10,20,30)}")
print(f"Sum: {calculate_total(10,20,30,40,50,60,70)}");

# kwargs: collects arguments into a dictionary

def show_details(**details):
    print(f"{details}");

show_details(name="Ayush Dutta", age = 25, job = "Embedded Systems Engineer");

# Local Variable: variable that can be accessed in a local environment

def calc():
    result = 100;
    print(result);

calc();

# print(result); NameError

tax_rate = 0.18;

def calc_tax(price):
    tax = price*tax_rate;
    return tax;

print(f"Tax: {calc_tax(50000)}");
print(f"Tax rate is {tax_rate}");

# fn and loops

def calc_total_list(numbers):
    total = 0;
    for num in numbers:
        total += num;

    return total;

numbers = [1,2,3,4,5,6,7];

print(f"Total: {calc_total_list(numbers)}");

# calculate average of list:

nums = [1,2,3,4,5,6,7];

def calc_average(numbers):
    total = 0;
    for i in numbers:
        total+=i;

    average = total/len(numbers);
    return average;

print(f"Average is: {calc_average(nums)}");

# Lambda: Anonymous Functions

square = lambda x: x**2;
print(f"Square: {square(5)}");





