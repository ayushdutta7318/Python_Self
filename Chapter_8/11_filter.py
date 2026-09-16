# Filter: applies a condition on iteralble and returns new filter object.

a = [1,3,90,45,0,63,37];

def is_greater_than_9(a):
    return a>9;

new_numbers = list(filter(is_greater_than_9, a));
print(new_numbers);

# aliter:
new_numbers_ = list(filter(lambda a: a>9, a));
print(new_numbers_);