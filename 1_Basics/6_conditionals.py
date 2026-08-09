# Conditionals:

"""
used in diecision making
"""

age = 15;

if age>=18:
    print(f"my age is {age} and i am an adult");
else:
    print(f"my gae is {age} and i am not adult");

# improper indentation leads to indentation error

age = int(input("enter you age: "));

if age>= 18:
    print(f"age is {age} and is an adult");
else:
    print(f"age is {age} and not an adult");

# elif
marks = float(input("Enter marks: "));

if marks>=90:
    print(f"marks is {marks} and grade A");
elif marks>=75 and marks<90:
    print(f"marks is {marks} and grade B");
else:
    print(f"marks is {marks} and grade C");

# nested if:
has_permission = True;

if age>=18:
    if has_permission:
        print("access granted");
else:
    print("access denied");

# aliter
if age>=18 and has_permission:
    print("access granted");
else:
    print("access denied");
