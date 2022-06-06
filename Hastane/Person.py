class Person:   #Person class'ı tanımlandı
    def __init__(self, tc, soyisim):   #tc ve soyisim parametreleri istendi.
        self.__tc = tc   #self ile tc ataması yapıldı.
        self.__soyisim = soyisim   #self ile soyisim ataması yapıldı.


    @property   #getter setter metodu kullanıldı.
    def tc(self):   #tc self ile fonksiyon olarak tanımlandı.
        return self.__tc  #return ile tc döndürüldü.

    @property   #getter setter metodu kullanıldı.
    def soyisim(self):  #soyisim self parametresi ile fonksiyon olarak tanımlandı.
        return self.__soyisim  #return ile soyisim döndürüldü.