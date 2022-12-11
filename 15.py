class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Операнд справа должен иметь тип int или Clock')
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.verify_data(other)
        return self.seconds <= sc

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 != 500) # если оператор __ne__ не реализован - то автоматически выполняется not(с1 == 500) - функция __eq__ инвертируется
print(c1 == 1000)
print(c1 == c2)
print(c1 < c2)
print(c1 > c2) # если оператор __gt__ не реализован - то ватоматически выполняется метод __lt__ - но операнды меняются между собой
