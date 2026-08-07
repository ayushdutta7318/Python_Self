# Input and Output Fn:

name_ = input("Enter name: ");
print(f"My name is : {name_}");

"""
How Input works:
Program Starts
      │
      ▼
Display Prompt
      │
      ▼
Wait for User Input
      │
      ▼
User Types Value
      │
      ▼
Store Value in Variable
      │
      ▼
Continue Program

input fn always returns str
"""
# Using f-Strings (Recommended)
print(f"{type(name_)}");
num = int(input("Enter #: "));
print(f"num: {num}, type: {type(num)}");