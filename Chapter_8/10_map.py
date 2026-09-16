# Map: Performs operation on iterable and return a new map object.

numbers = [46, 0, 97,2,1,7,89];

def square(x):
    return x*x;

new_numbers = map(square, numbers);
print(new_numbers);#returns map object

new_numbers = list(new_numbers);#will return a list
print(new_numbers);

# aliter
new_numbers_ = list(map(lambda a: a*a, numbers));
print(new_numbers_);