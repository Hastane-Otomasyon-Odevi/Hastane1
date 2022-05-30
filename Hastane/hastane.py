import pandas as pd
from Person import Person

class Hastane():
    def __init__(self):
        print("Hastanemize hosgeldiniz")
        self.__recordList = {}

    def menuSecim(self):
        cycle = True

        while cycle:
            try:
                secim = input("ekle : 1\nsil : 2\ngoster : 3\nLutfen yapmak istediginiz islemi secin: ").strip()
                while not (secim.isnumeric()) or int(secim) > 4 or int(secim) < 1:
                    secim = input("Gecersiz bir komut girildi, tekrar deneyin: ").strip()
            except Exception as e:
                print("Oops! ", e.__class__, " hatasi meydana geldi!")
            if secim == '1':
                self.hastaKayit()
            elif secim == '2':
                self.kayitSil()
            elif secim == '3':
                self.showAllRecords()
            else:
                print("Otomasyondan cikiliyor...")
                cycle = False

    def hastaKayit(self):
<<<<<<< HEAD
        tc = input("Hasta tcsi: ")
        soyad = input("Hasta soyismi: ")
        hasta = Patient(tc,soyad)
        print(hasta)
=======
       pass
>>>>>>> eac69d73f01420161c45d544d1c7ea7cc5c0b200
    def kayitSil(self):
        pass
    def showAllRecords(self):
        pass
    def hastaKontrol(self, no):
       pass


    @property
    #def recordList(self):
        

    @recordList.setter
    #def recordList(self, value):