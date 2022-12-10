class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def old(self):
        del self.__old

p = Person('Vasia', 20)
p.age = 30
print(p.age)