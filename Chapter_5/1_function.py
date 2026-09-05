# Defining Function: contains a piece of code which can be reused. code can perform a task or return a value

# lets find average of 3 number
a = 4;
b=3;
c = 1;
average = (a+b+c)/3;
print(average);

# but above is very troublesome if we need to make change in other cases
def average(a,b,c):
    d = (a+b+c)/3;
    # print(d);
    return d;

average(3,5,2);

# now if:
o1 = average(5,4,9);
o2 = average(19,8,4);
print(o1);#O/P: None: bcz fn average is not returning any value
print(o2);#O/P: None: bcz fn average is not returning any value

def greet(name):
    return f"hello, {name}";

print(greet("Alice"));