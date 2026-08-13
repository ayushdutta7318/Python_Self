# Dictionaries in python:

# list stores value by position:
"""
Index 0 → ID
Index 1 → Name
Index 2 → Age
"""
employee = ["EMP001", "Ayush Dutta", 28];
print(employee);

# Dictionary: A dictionary stores data as key-value pairs.

# syntax
employee = {
    "id": "EMP001",
    "name": "Ayush Dutta",
    "age": 28,
    "job": "Embedded Systems Engineer"
};
print(employee);
print(employee["job"]); #access dict element

# Dictionary are mutable:

employee = {
    "name": "ayush",
    "age": 28
};

employee["age"] = 25;
print(employee);

# adding a new key to exisiting dict:

employee["department"] = "data analytics";
print(employee);

# if we access key that does not exist: keyError

# get method
friends = {
    "friend_1":"Chandan",
    "friend_2": "Singhai",
    "friend_3": "harry",
}

print(friends.get("friend_3"));
print(friends.get("friend_4", 0));

# check if  a key exist:

if "age" in employee:
    print(True);

# or

if "bonus" not in employee:
    print(True);

# keys:
print(employee.keys());

# loop through keys:
for keys in employee.keys():
    print(keys);

# values
print(employee.values());
for value in employee.values():
    print(value);

# items: to print both key value:
print(employee.items());

for key, value in employee.items():
    print(f"{key}: {value}");

employee.update({
    "hobby": "horror movie",
});

print(employee);

# remove a key: pop: pop() removes the key and returns its value.
employee.pop("hobby");
print(employee);

# del
del employee["age"];
print(employee);

# remove everything from dict:
employee.clear();
print(employee);

# len
print(len(friends));

# Nested Dict:
employees = {
    "EMP_1": {"name": "ayush"},
    "EMP_2":{"name": "harry"},
    "EMP_3":{"name": "rohan"}
};

# list of dict:

employees = [
    {"name": "ayush", "age":28},
    {"name": "rohan", "age":30},
    {"name": "harry", "age":32},
]

for element in employees:
    print(element["name"]);

# filtering list of dict
for element in employees:
    if element["age"] > 30:
        print(element["name"]);

# dict comprehension:

numbers = [1,2,3,4,5];

squares = {
    number: number**2
    for number in numbers
}
print(squares);

num = range(1,11);
print(num);

# comprehension with condition
square_condition = {
    number: number**2
    for number in num
    if number %2 ==0
}

print(square_condition);

# count frequncies:
demo = ["ayush","rohan","ayush","harry", "ramesh","ramesh"];

count = {};

for el in demo:
    if el in count:
        count[el] += 1;
    else:
        count[el] = 1;

print(count);
