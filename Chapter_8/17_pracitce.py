# Practice set:

# decorators:

def logger(fn):
    def wrapper():
        print("fn is being called");
        fn();

    return wrapper;

@logger
def say_hello():
    print("Hello...");

say_hello();

# decorator:
import time
def timer(fn):
    def counter(a):
        start = time.time();
        result = fn(a);
        end = time.time();
        print(f"total time taken = {end - start: .6f} seconds");
        return result
    return counter;
        
@timer
def sum(a):
    total = 0;
    i = 1;
    while(i<=a):
        total += i;
        i+=1;

    return total;

sum(1000000);

# getter and setter:
class Employee:
    def __init__(self, salary):
        self._salary = salary;

    @property #getter
    def salary(self):
        return self._salary;

    @salary.setter #setter
    def get_salary(self, value):
        if(value< 0):
            print("Warning: salary cannot be negative");
        else:
            self._salary = value;

e1 = Employee(45000);
print(e1.get_salary);

e1.get_salary = 89000;
print(e1.get_salary);

# static and class method
class MathUtils:

    @staticmethod
    def add(a,b):
        return a+b;

    @classmethod
    def description(cls):
        print("this is a utility class for math operations.");

print(MathUtils.add(5,4));
MathUtils.description();

# dunder method:
class Book:
    def __init__(self, title, author):
        self.title = title;
        self.author = author;

    def __str__(self):
        return f"Book Title: {self.title}\nAuthor: {self.author}";

    def __len__(self):
        return len(self.title);

b1 = Book(title="Harry Potter", author="Ayush Dutta");
print(b1);
print(len(b1));

# exception handling
try:
    a = int(input("Enter num: "));
    print(f"user entered: {a}");
    b = int(input("enter num b:"));
    print(a/b);
except ValueError:
    print("not a number");
except ZeroDivisionError:
    print("cannot divide by zero");


# Custom error
class NegativeNumberError(Exception):
    ...

num = int(input("enter number: "));
if num<0:
    raise NegativeNumberError("Negative number not allowed");


