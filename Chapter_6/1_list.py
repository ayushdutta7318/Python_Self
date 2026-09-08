# List in Python: mutable data structure where multi values of diff datatypes can be stored

numbers = [54, 78, 36, 1, -2, 5]
mixed = [43, "hello", True, None, 57.9]
print(numbers)
print(mixed)

# accessign first and last element of list:
print(numbers[0])
# index starts from 0
print(numbers[len(numbers) - 1])

# print a chunk of data
print(numbers[1:3]);

# if index out of range
print(numbers[10]); #this produces error

