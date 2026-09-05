# Function arguments:

def add(a,b):
    return a+b;
print(add(3,7));

# aliter
def add_(a,b):
    sum = a+b;
    return sum;
print(add_(5,4));


#Default argument
def greet(name="ayush"):
    return f"hello, {name}";

print(greet());#even if we dont pass any argument, it will take default value and hence no error.
print(greet("harry"));
# parameter: parameter is the variable that we write while defining the fn, and arguments are actually specific values that we pass to the fn.

# Keyword argument: when we specify which value belongs to which parameter
c = add(b=3,a=7);
print(c);