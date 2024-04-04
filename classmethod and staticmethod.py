class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius):
        return radius > 0


circle = Circle.from_diameter(10)
area = circle.area()
print(f"Площа круга з радіусом {circle.radius} одиниць дорівнює {area} квадратних одиниць.")

valid = Circle.check_radius(17)
print(f"Радіус 17 є {'валідним' if valid else 'невалідним'}.")
