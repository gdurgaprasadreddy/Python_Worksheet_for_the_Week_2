import math
class Circle:
    def area(self, radius):
        return math.pi * radius * radius

class Rectangle:
    def area(self, length, breadth):
        return length * breadth

radius = float(input("Enter circle radius: "))
length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))

circle1 = Circle()
rectangle1 = Rectangle()
print("Circle Area:", round(circle1.area(radius), 2))
print("Rectangle Area:", rectangle1.area(length, breadth))
