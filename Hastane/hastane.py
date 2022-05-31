import pandas as pd   #Awesome Python kütüphanesinin kullanımı zorunlu olduğu için pandas'ı kullandık.
from Person import Person   #Person'dan veri çekebilmek için kullandık.

class Hastane():   #Hastane class'ı oluşturuldu.
    def __init__(self):
        print("Hastanemize hosgeldiniz")
        self.__recordList = {}

    def menuSecim(self):   #Menü seçim fonksiyonu oluşturuldu
        cycle = True   #While döngüsüne girebilmesi için True değeri atandı.

        while cycle:   #While döngüsüne girebilmesi için cycle'daki değer değerlendirildi.
            try:
                secim = input("ekle : 1\nsil : 2\ngoster : 3\nLutfen yapmak istediginiz islemi secin: ").strip()   #Seçim yapılabilmesi için input değer alındı, .strip metoduyla boşluklar silindi.
                while not (secim.isnumeric()) or int(secim) > 4 or int(secim) < 1:   #Seçimin sadece numaralardan ve istenilen aralıkta olması istendi ve while ile döngü kontrolü yapıldı.
                    secim = input("Gecersiz bir komut girildi, tekrar deneyin: ").strip()   #input ile değer alınmak istendi, seçime kayıt edildi ve .strip ile boşlukları alındı.
            except Exception as e: 
                print("Oops! ", e.__class__, " hatasi meydana geldi!")   #Meydana gelen hatayı ekrana yazdırmak için except kullanıldı.
            if secim == '1':  #Eğer seçimden gelen değer 1 ise Hasta kaydı oluşturlacak.
                self.hastaKayit()
            elif secim == '2':   #Eğer seçimden gelen değer 2 ise Hasta kaydı silinecek.
                self.kayitSil()
            elif secim == '3':   #Eğer seçimden gelen değer 3 ise showAllRecords fonksiyonu çalıştırılacak.
                self.showAllRecords()
            else:   #Seçim istenilen değeri girilmezse else çalışır.
                print("Otomasyondan cikiliyor...")   #Ekrana 'Otomasyondan çıkılıyor yazdırır.
                cycle = False   #Cycle değeri false olur.

    def hastaKayit(self):

        tc = input("Hasta tcsi: ")
        soyad = input("Hasta soyismi: ")
        hasta = Patient(tc,soyad)
        print(hasta)

       

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