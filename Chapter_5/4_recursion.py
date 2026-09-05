# Recursion: Function Calling itself to solve a problem

# 1.fibonaci

def fib(n):
    # base case
    if(n==0 or n==1):
        return n;

    return fib(n-2) + fib(n-1);

print(fib(3));

# factorial

'''
6! = 6*5*4*3*2*1

'''

def factorial(n):
    # base case:
    if(n==1 or n==0):
        return 1;

    return n*factorial(n-1);

print(factorial(5));
print(factorial(0));