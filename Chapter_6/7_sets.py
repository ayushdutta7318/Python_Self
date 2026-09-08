# Sets in  Python: Sets are unordereed unique collection of data.

s = {12,35,48,78};
print(f"set: {s}\ndatatype: {type(s)}");

# print(s[3]);#mot allowed as set is unordered.

# set methods:
s.add(45);
print(s);

a = {1,45,67};
b = {78,1,99};
print(a.union(b));
print(a.intersection(b));
print(a.difference(b));
print(b.difference(a));