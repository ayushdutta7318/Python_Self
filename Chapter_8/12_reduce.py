# Reduce:
from functools import reduce;

a = [1,2,3,4,5,6,7];

def sum(a,b):
    return a+b;

c = reduce(sum, a);
print(c);

# aliter
c_ = reduce(lambda a,b: a+b, a);
print(c_);