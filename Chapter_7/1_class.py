# Classes in Python: A class is a blueprint or template for creating objects, while an object is an instance of a class.

class Employee:
    company = "HP";

    def get_salary(self): #self refers to object created from a class
        print(self);
        return 34000;


ayush = Employee();
print(ayush.get_salary());
print(ayush.company);