# Dictionaries: data structure of key value pairs.

marks = {
    "Ayush": 98,
    "Sarah": 75,
    "Ramesh": 87
}

print(marks)
print(type(marks));

# access element in dictioanries:
print(marks["Ayush"]);

# modify values:
marks["Ayush"] = 100;
print(marks);

# methods
print(marks.keys());
print(marks.values());
# marks.clear();
# print(marks);

marks.pop("Sarah");
print(marks);