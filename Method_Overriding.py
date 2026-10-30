class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

dog1 = Dog()
cat1 = Cat()
dog1.sound()
cat1.sound()
