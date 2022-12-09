class Vector:
    MIN_COORD = 1
    MAX_COORD = 5

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def sqr(x):
        return x * x + Vector.MIN_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(2, 3)
