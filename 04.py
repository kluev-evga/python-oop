class Point:
    def __new__(cls):
        return super().__new__(cls)


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
