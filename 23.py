class Geom:
    def __init__(self, x):
        self.__x = x


class Rect(Geom):
    def __init__(self, x, y):
        super().__init__(x)
        self.__y = y


r = Rect(10, 20)
print(r.__dict__)
