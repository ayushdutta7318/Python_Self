# Loops in python:

# 1. for loop

for number in range(1,6):
    print(number);

for number in range(6):
    print(number);

for number in range(1,6,2):
    print(number);

# loop through a string:

name = "ayush";
for char in name:
    print(char);

# 2. while loop

num = 1;

while num <=5:
    print(num);
    num+=1;

# break and continue statements in loop

num = 1;
while num<=5:
    print(num);
    if num == 4:
        break; #breaks out of loop if condition met
    num+=1;

print("----continue----");
n = 1;
while n<=5:
    print(n);
    if n == 2:
        n+=1;
        continue; #skips loop
    n+=1;

# pass: when nothing is to be done
for i in range(1,6):
    pass;

# Q find max

li = [23, 71, 15, 92, 46, 38];

largest = li[0];

for num in li:
    if num > largest:
        largest = num;

print(largest);