from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

pt = Point(1,2)
pt.set_coord(10, 20)
# pt._Point__y = 1555
# pt._Point__x = 123123123
print(pt.__dict__)
print(pt.get_coord())

