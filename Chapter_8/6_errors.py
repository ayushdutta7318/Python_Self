# Errors in Python:

while True:
    try:
        a = int(input("Enter num 1: "));
        b = int(input("Enter num 2: "));
        print(f"division: {a / b}");

    except Exception as e:
        print(e);

    except ValueError:
        print("Please dont perform bad typecast");

    except ZeroDivisionError:
        print("dont divide by zero");




        