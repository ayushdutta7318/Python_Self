# Walrus Operator:

def very_slow_fn():
    print("Something...");
    print("Something...");
    print("Something...");
    print("Something...");
    print("Something...");
    return 70;

if (very_slow_fn() > 10):
    print(very_slow_fn());
else:
    print("not greater rthan 10");

# now if very_slow_fn() returns 70, then very_slow_fn will run twice, but we dont want it to execute twice.

if((a:=very_slow_fn()) > 10):
    print(a);
else:
    print("not greater rthan 10");

# one more application:
while(data:=input("enter: ")):
    print(data);
    if data == "q":
        break;