# Magic (Dunder) methods:

class Employee:
    #constructor: is called when the object(instance) is created
    def __init__(self, name, id, value, team_size):
        self.name = name;
        self.id = id;
        self.value = value;
        self.team_size = team_size;

    #__str__: controls what print() fn will display.
    def __str__(self):
        return f"The name is {self.name} and id is {self.id}";

    #__repr__: official string representation used for debugging
    def __repr__(self):
        return f"name: {self.name}\nid: {self.id}\nvalue: {self.value}\nteam size: {self.team_size}";

    #__add__: defines behavior for the + operator
    def __add__(self, other):
        return self.value + other.value;

    #__len__: defines behaviour for len().
    def __len__(self):
        return self.team_size;


ayush = Employee("Ayush", 123, 3, 7);
print(ayush);

ramesh = Employee("Ramesh", 456, 7, 3);

print(ayush + ramesh);
print(len(ayush));
print(len(ramesh));

print(repr(ayush));