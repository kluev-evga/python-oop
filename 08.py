class TreadData:
    __shared_attrs = {
        'name': 'tread_1',
        'data': {}
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

data_1 = TreadData()
data_2 = TreadData()
data_1.id = '123'

print(data_1.__dict__)