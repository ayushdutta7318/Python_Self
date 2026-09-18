# Writing to a file: we can write to a file, but as soon as we write another set of text, the older one gets erased.

f = open("write_2.txt", "w");

string = '''I am ayush dutta, 
i love embedded systems,
i love programming hardware.
'''

f.write(string);
f.close()