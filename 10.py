from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.age = age
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) !=3:
            raise TypeError('Неверный формат записи')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотябы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError('Возраст должен быть числом  в диапазоне [14; 120]')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вес должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')
        s = ps.split()
        if len(s) != 2 or len(s[0]) !=4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должен быть числом')

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        self.verify_age(age)
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @age.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @age.setter
    def weight(self, ps):
        self.verify_weight(ps)
        self.__ps = ps

p = Person('Пупкин Василий Васильевич', 30, '1234 567890', 80.0)
print(p.__dict__)