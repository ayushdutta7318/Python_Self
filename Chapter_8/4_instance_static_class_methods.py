# Instance, static and class methods in Python:

class Employee:
    company = "Dell"

    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
    # 1. Instance method
    def print_info(self):
        info = f"The Employee name is {self.name} and salary is {self.salary}";
        print(info);

    # 2.
    # def sum(self, a,b):
    #     return a+b;

    # 4.
    @staticmethod #static method does not require "self" object
    def sum(a,b):
        return a+b;

    # 5. Class methods
    @classmethod
    def print_company(cls):
        print(cls.company);

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company;

jack = Employee("Jack", 45000);
jill = Employee("Jill", 58000);

# 3. when we print info: everything works well
jack.print_info();
jill.print_info();

#but when we print sum(); we get error
print(jack.sum(3,7));

"""
TypeError: Employee.sum() takes 2 positional arguments but 3 were given, bcz the 3rd arg is "self" object. we can make it work by writing def sum(self, a, b):

But we will rather use @staticmethod. Static methods are those methods which do not need a "self" object
"""

# class methods:
print(jack.company);

Employee.print_company();

jack.change_company("Acer");
jack.print_company();

Employee.change_company("Huawei");
jack.print_company();