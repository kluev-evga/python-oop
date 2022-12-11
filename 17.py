class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x + self.y

    def __bool__(self):
        return self.x == self.y

p = Point(1, 10)
print(bool(p))