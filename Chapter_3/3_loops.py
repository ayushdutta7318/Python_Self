# loops:

# lets print from 1 to 5
print(1);
print(2);
print(3);
print(4);
print(5);

# lets automate above:
for i in range(1,6):
    print(f"The value of i is: {i}");

#range() is fn which goes from 1..5.

# print the table of 5:
for i in range(1,11):
    print(f"{5} * {i} = {5*i}");

# for loop in list: List(later)
friends = ["ayush", "ramesh", "suresh"];
for friend in friends:
    print(f"friend is: {friend}");

# While Loop:

a = 1;
while(a<=5):
    print(f"value of a: {a} ");
    a+=1;

# Infinite loop: when we dont have an update in the value of var inside loop
b = 1;
while(b<=5):
    print(b);
    #no update in the value of var b.

