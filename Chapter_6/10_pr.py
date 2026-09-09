# Practice Set:

# 1.
fruits = ["apple", "banana", "cherry"];
print(fruits[0]);
fruits[1] = "orange";
print(fruits);
print(len(fruits));

# 2.
numbers = [a for a in range(1,11)];
print(numbers);

# 3
li = [55,3,-2,45,11,4,700,67];
li.sort();
print(li);

li.append(10);
print(li);

li.remove(11);
print(li);

# ttuple
coordinates = (10,20);
for el in coordinates:
    print(el);

li_ = list(coordinates);
print(li_);

li_[0] = 50;
coordinates_ = tuple(li_);
print(coordinates_);

# set
my_set = {1,2,3,3,5};
print(my_set);

my_set.add(4);
my_set.remove(2);
print(my_set);

a = {1,2,3};
b = {3,4,5};
print(a.intersection(b));
print(a.union(b));
print(a.difference(b));

# dictionaries
student = {
    "name": "John Doe",
    "age": 28,
    "grade": "A"
};

print(student["name"]);
student["grade"] = "A+";
print(student);
student["city"] = "Indore";
print(student);

# 
friends = {
    "ayush": 123,
    "ramesh": 456,
    "suresh": 789
};

print(friends.keys());
print(friends.values());
print(friends.items());

# bonus

num = [1,3,3,5,5,7];
num = set(num);
print(num);

products_prices = {
    "monitor": 8000,
    "mini PC": 81000,
    "keyboard-mouse": 3400
}

max_price = 0
for key, value in products_prices.items():
    print(f"{key}: {value}");
    if(max_price<value):
        max_price = value;

print(max_price);

d1 = {
    "name": "harry"
}
d2= {
    "job":"teacher"
}
merged = d1 | d2;
print(merged);