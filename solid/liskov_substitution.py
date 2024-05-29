# LSP

# Liskov Substitution Principle
# - You should be able to substitute a base type for a subtype
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


# class that break Liskov principle
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # the problem is here
    expected = int(w * 10)
    print(f'Expected an are of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

# break Liskov principle

sq = Square(5)
use_it(sq)
