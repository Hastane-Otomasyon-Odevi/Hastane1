class Person:
    def __init__(self, tc, soyisim):
        self.__tc = tc
        self.__soyisim = soyisim


    @property
    def tc(self):
        return self.__tc

    @property
    def soyisim(self):
        return self.__soyisim