# Inheritance:

class Animal:
    # class attrirbute
    location = "indore";

    def __init__(self, name):
        self.name = name;

    def speak(self):
        print("generic animal sound");

class Dog(Animal):
    def speak(self):
        super().speak();
        print("woof");

class Cat(Animal):
    def speak(self):
        super().speak();
        print("meow!");


# create instance:
my_dog = Dog("goofy");
my_cat = Cat("tom");

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name);
print(my_cat.name);

# They both have a 'speak' method, but it behaves differently:
my_cat.speak();
my_dog.speak();
# if we want speak fn from parent class, we use "super" keyword

# class attribute of parent class animal
print(my_cat.location);
print(my_dog.location);