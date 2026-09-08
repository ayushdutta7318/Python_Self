# Tuple: Immutable. similar to list

t = (78,95,13,45,64);
print(t);

# access tuple element:
print(t[0])
print(t[len(t)-1]);

# t[0] = 789;# type error

# create tuple with 1 element

one_element = (45,);
print(type(one_element), one_element);