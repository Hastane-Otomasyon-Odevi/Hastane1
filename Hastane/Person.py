class Person:   #Person class'ı tanımlandı
    def __init__(self, tc, soyisim):   #tc ve soyisim parametreleri istendi.
        self.__tc = tc   #self ile tc ataması yapıldı.
        self.__soyisim = soyisim   #self ile soyisim ataması yapıldı.


    @property   #getter setter metodu kullanıldı.
    def tc(self):   
        return self.__tc

    @property   #getter setter metodu kullanıldı.
    def soyisim(self):
        return self.__soyisim