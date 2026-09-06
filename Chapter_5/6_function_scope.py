# Fucntion scope:

# lets say
def sum(a,b):
    # c, a and b are local variables and are destroyed as soon as the fn returns a value
    c = a+b;
    print(z);
    # if
    z = 1; #this is a local var and gets destroyed as soon as the function returns
    return c;

# lets define global var: global var can be accessed anywhere
z = 8;

print(sum(3,7));
# but if i try to access c here:
# print(c); Name Error


