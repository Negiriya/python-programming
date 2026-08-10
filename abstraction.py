from abc import ABC, abstractmethod


# Abstract Class

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child Class

class Car(Vehicle):

    def start(self):
        print("Car starts with a key.")


class ElectricCar(Vehicle):

    def start(self):
        print("Electric car starts with a button.")


# Creating Objects

car = Car()
electric_car = ElectricCar()

car.start()
electric_car.start()
