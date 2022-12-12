class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def lentgth(self):
        return self.__lenght

    @lentgth.setter
    def length(self, value):
        self.__length = value

class point2D(Point):
    pass

class point2D(Point):
    __slots__ = ()

pt = Point2D(10,20)
pt.z = 30