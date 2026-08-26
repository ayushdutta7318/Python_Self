# Typecastign in python:

# type() fn: tells about datatype of the value refered by var

a = 34;
print(f"a: {a}, datatype of a: {type(a)}");

b = "34";
print(f"b: {b}, datatyep of b: {type(b)}");

c = int(b);
print(f"c: {c}, datatype of: {type(c)}");

# but what if:
d = "ayush"
# e = int(d); # value error:

# convert num to str
e = 45;
f = str(e);
print(f"e: {e}, datatype: {type(e)}");
print(f"f: {f}, datatype: {type(f)}");

# cpnvert float to int
pi = 3.14;
int_pi = int(pi); #o/p: 3
print(int_pi);