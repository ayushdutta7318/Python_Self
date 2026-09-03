# Comments, escape sequence

print("hello, world!");

# this is a single line comment

"""
this is a multi line comment
"""

'''
this is also multi line comment
'''

# print("hello
# world") syntax error

print("hello\nayush how\nare you");
# or
print("""hello 
ayush how are
you""")

print("hello bhai, how \\are you, i \tam good");

# we also use scape sequence to print a double quote in a double quote
print("hello \"how\" are you");

# print multiple things
print('hellow wolrd', "Ayush",5);
# sep: default value is " "
print('hellow wolrd', "Ayush",5, sep=",");
# end: default value is \n
print("hello, world", "ayush", end="\t");
print("hello");
