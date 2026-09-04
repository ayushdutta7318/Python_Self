# Practice Set:

# 1.
i = int(input("enter num: "));
if i>0:
    print(f"{i} is positive");
elif i == 0:
    print(f"{i} is neutral");
else:
    print(f"{i} is negative");

# 2
age = int(input("enter age: "));
if age>=18:
    print("you can vote");
else:
    print(f"you have to wait {18-age} years to vote");

# 3. check even num
num = int(input("enter num: "));
if num%2==0:
    print(f"{num} is even");
else:
    print(f"{num} is odd");


# 4. match day

day = 3;
match day:
    case 1:
        print("monday");
    case 2:
        print("tuesday");
    case 3:
        print("wednesday");

    case _:
        print("sunday");


# 5.
num_1 = int(input("enter num 1: "));
num_2 = int(input("enter num 2: "));
operation = input("enter opertation: ");

match operation:
    case "+":
        print(f"num_1 + num_2: {num_1+num_2}");
    case "-":
        print(f"num_1 - num_2: {num_1-num_2}");
    case "*":
        print(f"num_1 * num_2: {num_1*num_2}");
    case "/":
        print(f"num_1 / num_2: {num_1/num_2}");

    case _:
        print("invalid operation");

