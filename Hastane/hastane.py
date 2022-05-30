from cmath import e
from Patiant import Patient

class Hastane():
                            #Liste olusturulacak 
    def __init__ (self,ad):
        self.ad = ad
        self.calisma = True # her zaman çalışır durumda sağlamak için
    def program(self):
        secim = self.menuSecim()

    def menuSecim(self):
        while True: # seçim istenilen aralığın dışında kalmaması için önlem
            try:
                secim = int(input("**** {} hastahenemize hos geldiniz\n\n1-Hasta Kayit\n2-Hasta Sil\n\nSecimizi Giriniz : ".format(self.ad))) # istenen deger tam sayı olması saglandı
            except ValueError:
                print("Lutfen gecerli bir deger giriniz.")
            
            if secim == 1:
                self.hastaKayit()
                    
    def hastaKayit(self):
        tc = input("Hasta tcsi: ")
        soyad = input("Hasta soyismi: ")
        hasta = Patient(tc,soyad)
        print(hasta)
    def kayitSil(self):
        pass

hastane = Hastane("Bunyamin Hastanesi") # obje tanımlaması

while True: # true deger alarak çalışır durumda tutmak için
    hastane.program()
