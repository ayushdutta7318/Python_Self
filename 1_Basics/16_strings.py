#Strings in python:

"""
immutable and are sequence of characters
"""

name = "ayush";
print(name);

# access string element
print(name[0]);

# immmutable:
# name[0]  = "A"; #TypeError

# instead create a new string

name_ = "A" + name[1:]
print(name_);

# multi line string
print(f'''My name
is 
{name_}''');

# indexing: positive

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]); #index error:

# negative indexing:
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

# access last char
print(name[len(name)-1]);
# or
print(name[-1]);

# length of string:
print(len(name));

# slicing
print(name[0:3:2]);

# reversing a str:
print(name[::-1]);

# strings are immutable, but:

name = "ayush";
# name[0] = "v"
# but
name = "rahul"
print(name); #name is now refering to rahul, rather than ayush and older str gets cleaned up by python's memoty mgmt

# membership operator: in and not in

friend = "ramesh";
print("ram" in friend);
print("am" in friend);
print("am" not in friend);

# string methods:

"""
lower()
upper()
title()
capitalize()
swapcase()

strip()
lstrip()
rstrip()

replace()
split()
join()

find()
index()
count()

startswith()
endswith()

isdigit()
isalpha()
isalnum()
isspace()
"""

# lower, upper, title:
str_ = "   ABcde   ";
print(str_.lower());
print(str_.upper());
print(str_.title());#useful in cleaning  names
print(str_.capitalize());
print(str_.strip());

# replace
text = "I love Java";
text = text.replace("Java", "Python");
print(text);

# split()
print(text.split(" "));

# join
words = ["Python", "is", "powerful"]
print(" ".join(words));

# find
print(text.find("Python"));

# starts with: useful in dealing with files
print(text.startswith("I love"));

file_name = "ayush.csv";
print(file_name.endswith(".csv"));

# string validation: ai

# escape char:
print("He said \"Hello\"");
print("hello \nworld");

# raw strings: Raw strings are useful when backslashes should be treated literally.

path = r"A:\Programming\Python_2\1_Basics"
print(path);

# formatted string:
name = "ayush";
number = 19;
print(f"My name is {name}, my number {number}");

# expressions inside f-strings:
price = 5;
quantity = 100;
print(f"{(price*quantity): .3f}".strip());

# string iteration:

text = "kb vkdfbvkfdjvdkfnv vcnlofjdknvdfnv ";
for char in text:
    print(char);

# or

for i in range(len(text)):
    print(f"{i+1}: {text[i]}");

# data cleaning eg:

cleaned = [];

countries = [
    "india", "  US  ", "China   "
];

for country in countries:
    country = country.strip();
    country = country.capitalize();
    cleaned.append(country);

print(cleaned);