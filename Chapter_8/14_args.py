# Args:

def sum(*args):
    print(args);
    total = 0;
    for el in args:
        total += el;
    return total;

print(sum(134,34,96));