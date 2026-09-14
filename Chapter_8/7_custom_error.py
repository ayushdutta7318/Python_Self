# Custom Error

a = int(input("enter a: "))
b = int(input("enter b: "))

if b == 0:
    raise ValueError("bhai mat kar divide 0 se");

print(f"division: {a/b}");
