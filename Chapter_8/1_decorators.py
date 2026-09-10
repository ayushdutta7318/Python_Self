# Decorators in python: Decorator is a function that takes a function as an argumnent, then creates a new function inside its body and then returns that new function.

def decorator(fn):
    def wrapper():
        print("I am going to print hello...");
        fn();
        print("I am done priting hello...");

    return wrapper;

def say_hello():
    print("Hello");

# say_hello()

decorator(say_hello);

f = decorator(say_hello);
f();

# aliter of line 18:
@decorator
def greet():
    print("hello!");

greet();