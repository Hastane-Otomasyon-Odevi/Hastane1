import pandas as pd   #Awesome Python kutuphanesinin kullanimi zorunlu oldugu icin pandas'i kullandik.
from Person import Person   #Person'dan veri cekebilmek icin kullandik.

class Hastane():   #Hastane class'i olusturuldu.
    def __init__(self):
        print("Hastanemize hosgeldiniz")
        self.__recordList = {}

    def menuSecim(self):   #Menu secim fonksiyonu olusturuldu
        cycle = True   #While dongusune girebilmesi icin True degeri atandi.

        while cycle:   #While dongusune girebilmesi icin cycle'daki deger degerlendirildi.
            try:
                secim = input("ekle : 1\nsil : 2\ngoster : 3\nLutfen yapmak istediginiz islemi secin: ").strip()   #Secim yapilabilmesi icin input deger alindi, .strip metoduyla boşluklar silindi.
                while not (secim.isnumeric()) or int(secim) > 4 or int(secim) < 1:   #Secimin sadece numaralardan ve istenilen aralikta olmasi istendi ve while ile dongu kontrolu yapıldı.
                    secim = input("Gecersiz bir komut girildi, tekrar deneyin: ").strip()   #input ile deger alinmak istendi, secime kayit edildi ve strip ile bosluklari alindi.
            except Exception as e: 
                print("Oops! ", e.__class__, " hatasi meydana geldi!")   #Meydana gelen hatayi ekrana yazdirmak icin except kullanildi.
            if secim == '1':  #Eger secimden gelen deger 1 ise Hasta kaydi olusturulacak.
                self.hastaKayit()
            elif secim == '2':   #Eger secimden gelen deger 2 ise Hasta kaydi silinecek.
                self.kayitSil()
            elif secim == '3':   #Eger secimden gelen deger 3 ise showAllRecords fonksiyonu calistirilacak.
                self.showAllRecords()
            else:   #Secim istenilen degeri girilmezse else calisir.
                print("Otomasyondan cikiliyor...")   #Ekrana 'Otomasyondan cikiliyor yazdirir.
                cycle = False   #Cycle degeri false olur.

    def hastaKayit(self):   #Hasta kayıt fonksiyonu oluşturuldu.
        tc = input("Hastanin tc'sini giriniz: ")
        while not(tc.isnumeric()) or len(tc) < 11 or len(tc) > 11:
            tc = input("Hastanin 11 haneli tc'sini giriniz: ")

        soyIsim = input("Soyismi giriniz:")
        while not(soyIsim.isalpha()):
            soyIsim = input("Soyisim rakam veya baska bir karakter iceremez tekrar deneyiniz: ")
            print()

        if self.hastaKontrol(tc):
            self.recordList[tc] = soyIsim
            print("Hasta sisteme kaydedildi!")
        else:
            print("Sistemde bu tc'de kayitli bir hasta var!")


    def kayitSil(self):   #Seçime göre kayıt silme fonksiyonu çalışır.
        delTc = input("Silinmek istenen hastanin tc si :")
        if not (self.hastaKontrol(delTc)):
            self.recordList.pop(delTc)
        else:
            print("Boyle bir kayit bulunamadi!")
            print("Tekrar Kontrol Edebilirsiniz")

    def showAllRecords(self):   #Seçime göre showAllRecords fonksiyonu çalışır.
        pass
    def hastaKontrol(self, no):   #Seçime göre hasta kontrol fonksiyoru çalışır.
       pass


    @property   #Getter Setter metodu kullanılmaya çalışıldı.
    #def recordList(self):
        

    @recordList.setter   #Getter Setter metodu kullanılmaya çalışıldı.
    #def recordList(self, value):