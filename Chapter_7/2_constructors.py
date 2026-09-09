# Constructor:

class Employee:
    def __init__(self, name, salary, bond):
        self.name = name; #this line means create an attribute and assign the value as name
        self.salary = salary;
        self.bond = bond;

    def get_info(self):
        print(f"The name of employee is {self.name}, his salary is {self.salary} and his bond is {self.bond} years");

    def get_salary(self):
        ...

ayush = Employee("ayush dutta", 100000, 1);
print(ayush.bond);
ayush.get_info();
        