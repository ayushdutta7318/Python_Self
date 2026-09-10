# Practice set:

# 1. class and object

class Car:
    def __init__(self):
        pass

    def drive(self):
        print("car is moving...");


my_car = Car();
my_car.drive();

# 2. constructor

class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def get_info(self):
        print(f"My name is {self.name} and my age is {self.age}");

person = Person("person", 10);
person.get_info();

# inheritance
class Animal:
    def make_sound(self):
        print("some sound");

class Dog(Animal):
    def make_sound(self):
        super().make_sound();
        print("bark");

my_dog = Dog();
my_dog.make_sound();