class Point:
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """метод вызывается только при обращении к несущетсвующему свойству"""
        print('__getattr__: ' + item)

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt = Point()
pt.x = 5
print(pt.y)
# pt.__dict__ = {
#     'a': 10
# }
print(pt.__dict__)
