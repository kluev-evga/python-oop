class Point():
    def set_coords(self, x, y):
        self.x = x
        self.y = y


Point.set_coords(Point, 5, 10)

pt = Point()
f = getattr(pt, 'set_coords')
f(1, 2)

# Point.set_coords(Point, 1,3)
