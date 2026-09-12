# Getters in Python:

class Employee:
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;

    @property #this is a getter: @property is in built decorator
    def first_name(self):
        first = self.name.split(" ");
        return first[0];

    # to set first name:
    @first_name.setter #this is a setter
    def first_name(self, first):
        last = self.name.split(" ");
        new_name = f"{first} {last[1]}";
        self.name = new_name;



e = Employee("John Doe", 100000);
e.projects = 7; #setting an attribute
print(e.projects);

#prinitng first name of employee e:
print(e.name[0:e.name.find(" ")]);# method 1

# aliter: see in class body
# print(e.first_name());

# setfirst name:
# e.set_first_name("Jack");
print(e.name);


print(e.first_name); #note that first_name is a fn but not called like first_name(). parentheses are missing.

# also, if we talk about setter
e.first_name = "Ayush";
print(e.name);