# Reading Files content line by line:

f = open("ayush_1.txt", "r");

# content = f.read();
# print(content);

# read line by line:
for line in f:
    print(line);

f.close()