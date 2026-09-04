# String Slicing: taking out a chunk of chars from an str

name = "ayush";
print(name[0:2]); #goes from 0 to 2-1 = 1

# slicing with negative index:
print(name[1:-1]);

# adding steps in slicing:
sentence = "abcdefghijklmnopqrstuvwxyz";
print(sentence[0:len(sentence)-1:2]);
