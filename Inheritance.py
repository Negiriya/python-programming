# Inheritance

class Person:

    def introduce(self):
        print("I am a person.")


class Student(Person):

    def study(self):
        print("I am studying Python.")


# Creating Student Object

student1 = Student()

student1.introduce()
student1.study()


# Inheritance with Constructor

class Animal:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Animal:", self.name)


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


dog1 = Dog("Bruno")

dog1.show_name()
dog1.bark()
