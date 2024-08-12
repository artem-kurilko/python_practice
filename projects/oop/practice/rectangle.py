
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


r = Rectangle(5, 10)
print(r.area)
print(r.perimeter)