# if-elif-else statement:

age = int(input("Enter your age: "));

if age > 25:
    print(f"your age is {age} and hence you can drive"); #empty space is indentation and tells python interpreter that this line is inside if block
else:
    print("You cannot drive...");



# elif: multiple condition

if(age>18):
    print("you can drive");
elif(age == 18):
    print("you can do interview");
elif(age == 0):
    print("you are just born");
else:
    print("you cannot drive...");
