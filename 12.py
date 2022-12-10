class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


c = Counter()
c()


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)

s1 = StripChars('?:!.; ')
res = s1(' Hello World!? ')
print(res)


@StripChars
def strip(string):
    return string

print(StripChars('?:!.; ')(' Hello World!? '))