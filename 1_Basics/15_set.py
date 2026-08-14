# Sets in Python:

# data structure to store unique values

numbers = {10, 45,68, 78,15, 10, 45};
print(numbers);

# create a set using

friends = set(); #EMPTY SET

# dont use {} to create empty set, as it creates empty

num = {};
print(type(num));

# to filter out unique cvalues:

nums = [10,20,20,20,30,30,45,10,15];
unique_nums = set(nums);
print(unique_nums);

# sets are unordered

# print(unique_nums[0]); type error

# sets are mutable
unique_nums.add(59);
print(unique_nums);

# add single elemnt

unique_nums.add(78);

# add multiple element
unique_nums.update([789,1564,415614]);
print(unique_nums);

# remove element
unique_nums.remove(415614);
print(unique_nums);

# aliter: .discard: doent produce error:
unique_nums.discard(159789); #random number removed
print(unique_nums);

# .clear: removes everything
unique_nums.clear();
print(unique_nums);

# set operations: VVIP

A = {1,2,3,4,5};
B = {4,5,6,7,8};

# Uninion: returns everything w/o duplicates:
print(A|B);

# A intersection B
print(A.intersection(B));

# Difference:
print(A-B);#return elements A not in B

# reverse difference:
print(B-A);

# Symmetric Difference:
print(A.symmetric_difference(B));

# membership testing:
print(5 in A);

