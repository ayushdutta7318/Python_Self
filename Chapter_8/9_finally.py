# Finally

def divide(a,b):
# a = int(input("enter a: "))
# b = int(input("enter b: "))

    try:
        c = a/b;
        return c

    except Exception as e:
        return e;

    #this line si always excuted even if there is error or not, we have finally keyword so that if the result is returned inside fn.
    finally:
        print("this is always executed");

print(divide(8,5));
print(divide(8,0));