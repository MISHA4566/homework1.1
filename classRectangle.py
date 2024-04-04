class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(2, 4)


square = rect.area()
perimeter = rect.perimeter()

print(f'Площа прямокутника: {square}')
print(f'Периметр прямокутника: {perimeter}')
