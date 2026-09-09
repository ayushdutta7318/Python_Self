# Instance attributes v/s class attributes:

class Employee:
    company = "HP"; #class attribute

    def __init__(self, name, salary, bond, company):
        self.name = name; #this line means create an instance attribute and assign the value as name
        self.salary = salary;
        self.bond = bond;
        self.company = company;


    def get_info(self):
        print(f"The name of employee is {self.name}, his salary is {self.salary} and his bond is {self.bond} years and his company is {self.company} Tech.");

    def get_salary(self):
        ...

ayush = Employee("ayush dutta", 100000, 1, "HCL"); #instance attribute is give preference over class attribute
print(ayush.bond);
ayush.get_info();

harry = Employee("harry", 100000, 3, "TSMC");
harry.get_info();

print(Employee.company);