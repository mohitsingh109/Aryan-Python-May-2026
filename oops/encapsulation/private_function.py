class Test:
    def __init__(self, value):
        self.__value = value # private variable

    def __private_method(self): # private method
        print(self.__value)

    def get_value(self):
        return self.__value


t1 = Test(100)
print(t1.get_value())