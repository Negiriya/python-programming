# Polymorphism
# Same method name, different behavior

class Dog:

    def sound(self):
        print("Dog says: Woof!")


class Cat:

    def sound(self):
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Polymorphism using a common function

def make_sound(animal):
    animal.sound()


make_sound(dog)
make_sound(cat)


# Method Overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
