# String Indexing: this is how you access string elements

name = "Ayush";
print(name[0]);
print(name[1]);
print(name[2]);
print(name[3]);
print(name[4]);

# access last char in str:
print("--------------Negative Indexing---------------");
print(name[-1]);
print(name[-2]);
print(name[-3]);
print(name[-4]);
print(name[-5]);


"""
A   y   u   s   h
0   1   2   3   4
-5  -4  -3  -2  -1
"""

# Evaluating value inside brackets
print("-----------Evaluation iside brackets-----------");
print(name[1+3]);

# access last char in str:
print(name[len(name)-1])