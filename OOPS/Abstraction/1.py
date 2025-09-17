from abc import ABC , abstractmethod
class Vehcile(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehcile):
    def start(self):
        print('car starts with key')
class bike(Vehcile):
    def start(self):
        print("Bike starts with button")
           
Car = car()
Bike= bike()

Car.start()
Bike.start()