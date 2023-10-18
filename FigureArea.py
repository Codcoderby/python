import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def get_shape_input():
    shape_type = input("Fiquru daxil edin (dairə, düzbucaqlı və ya üçbucaq): ").lower()

    if shape_type == "dairə":
        radius = float(input("Dairənin radiusunu daxil edin: "))
        return Circle(radius)
    elif shape_type == "düzbucaqlı":
        width = float(input("Düzbucaqlının enini daxil edin: "))
        height = float(input("Düzbucaqlının hündürlüyünü daxil edin: "))
        return Rectangle(width, height)
    elif shape_type == "üçbucaq":
        base = float(input("Üçbucağın əsasını daxil edin: "))
        height = float(input("Üçbucağın hündürlüyünü daxil edin: "))
        return Triangle(base, height)
    else:
        print("Fiqurun adını düzgün daxil edin! ")
        return None

shape = get_shape_input()

if shape:
   
    print(f"{shape.__class__.__name__} Sahəsi: {shape.area()}")
