class Frange:

    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = Frange(0, 2, 0.5)

fr.__iter__()
print(next(fr))
print(next(fr))

for i in fr:
    print(i)


rng = range(0, 10, 1)
rng_nxt = rng.__iter__()
print(rng_nxt.__next__())


class Frange2D:

    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = Frange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr2 = Frange2D(0, 3, 0.5, 3)
for row in fr2:
    for x in row:
        print(x, end=' ')
    print()
