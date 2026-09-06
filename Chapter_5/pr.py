# Practice set:

# 1.
def greet():
    print("hello, python learner");

greet();

# square of num
square = lambda x: x*x;
print(square(3))
print(square(5))
print(square(7))

# full name function
full_name = lambda first_name, last_name: f"{first_name} {last_name}";
print(full_name("Ayush", "Dutta"));

def calculate_area(length, width=10):
    return length * width;

print(calculate_area(5,8));
print(calculate_area(5));

num = [1,2,3,4,5];
square_num = map(lambda x: x*x, num);
print(list(square_num));

# sum of n digit
def sum_digits(n):
    # Base case:
    if (n<10):
        return n;

    return (n%10) + sum_digits(n//10);

print(sum_digits(25)); #o/p 7
print(sum_digits(2589));#o/p 24

# gloabl var
counter = 0;

def increase_counter():
    global counter;
    counter += 1;
    return 0;

increase_counter();
print(counter);

increase_counter();
print(counter);

increase_counter();
print(counter);

increase_counter();
print(counter);

increase_counter();
print(counter);

# import local file
import myutils;
print(myutils.is_even(10));
print(myutils.is_even(7));