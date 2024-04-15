class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


def use_it(rc):
    w = rc.width
    rc.height = 10
    print(w, str(rc))


rc = Rectangle(2, 3)
use_it(rc)
