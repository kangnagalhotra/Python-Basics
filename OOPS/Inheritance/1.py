class Animal():
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog Barks")
        
dog = Dog()
dog.speak()
dog.bark()
