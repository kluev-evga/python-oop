class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getattr__(self, item):
        if 0 <= item <= self.marks[item]:
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым положительным числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым положительным числом')
        del self.marks[key]


s1 = Student('Вася', [5, 5, 3, 2, 5])
del s1[2]
s1[10] = 4
print(s1.marks)
