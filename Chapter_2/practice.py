# 1.
print("hello, welcome to python bootcamp");

# 2
print("""tweinkle twenlku
little star""");

# 3
name = "ayush";
age = 28;
job = "embedded systems";

print(f"my name is {name}, my age {age}, and i am a {job}");

# 4
num = "45";
num = int(num) + 5;
print(f"num is {num}");

# 5
food = input("enter fav food: ");
print(f"my fav food is {food}");

# 6
num_1 = int(input("enter num_1: "));
num_2 = int(input("enter num_2: "));

print(f"sum: {num_1 + num_2}");
print(f"difference: {num_1 - num_2}");
print(f"product: {num_1 * num_2}");
print(f"quotient: {(num_1 / num_2): 0.2f}");