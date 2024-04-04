class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)


circle = Circle(10)
area = circle.area()
print(f"Площа круга з радіусом {circle.radius} одиниць дорівнює {area} квадратних одиниць.")
