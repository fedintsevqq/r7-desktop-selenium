class TestCase:
    def __init__(self, name):
        self.__name = name
        self.__passed = False
        self.__err = 'Тест не выполнялся'

    @property
    def name(self):
        return self.__name

    @property
    def passed(self):
        return self.__passed

    @passed.setter
    def passed(self, passed):
        if type(passed) is bool:
            self.__passed = passed
        else:
            raise ValueError('Недопустимое значение passed')

    @property
    def error(self):
        return self.__err

    @error.setter
    def error(self, error):
        self.__err = str(error)