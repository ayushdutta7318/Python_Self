# Global Keywiord:

z = 10; #global var

def sum(a,b):
    c = a+b;
    global z; # this means global var can be modified
    z = 484; #z = 5 is the o/p
    return c;

print(sum(3,5));
print(z); #o/p = 5
