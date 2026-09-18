# Append to a file: write to an exisiting file  that already contains data.

f = open("write_2.txt", "a");

appnended_string = '''
i love dosa,
bcz i am south indian
'''

f.write(appnended_string);
f.close();