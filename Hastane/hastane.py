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
        tc = input("Hastanin tc'sini giriniz: ")   #input ile hastanın kimlik numarası alındı ve tc'ye kaydedildi.
        while not(tc.isnumeric()) or len(tc) < 11 or len(tc) > 11:  #while döngüsü ile kimlik numarasının 11 haneli ve sadece numaralardan oluşması koşullandırıldı.
            tc = input("Hastanin 11 haneli tc'sini giriniz: ")   #eğer 11 haneli değilse input ile tekrardan 11 haneli kimlik numarası istenir.

        soyIsim = input("Soyismi giriniz:")   #input ile hastanın soyismi alındı ve soyisim olarak kaydedildi.
        while not(soyIsim.isalpha()):    #soyismin sadece harflerden oluşması koşullandırıldı.
            soyIsim = input("Soyisim rakam veya baska bir karakter iceremez tekrar deneyiniz: ")   #input ile hastanın soyadı istendi ve soyisim olarak kaydedildi.
            print()   

        if self.hastaKontrol(tc):   #kimlik numarası doğru ise hasta kontrol ve burası çalışır. 
            self.recordList[tc] = soyIsim   #Self kullanıldı.
            print("Hasta sisteme kaydedildi!")   #Ekrana yazdırdı.
        else:
            print("Sistemde bu tc'de kayitli bir hasta var!")   #Şartlar sağlanmadıysa bu satır yazdırıldı.


    def kayitSil(self):   #Seçime göre kayıt silme fonksiyonu çalışır.
        delTc = input("Silinmek istenen hastanin tc si :")   #input ile kayıdı silinmek istenen hastanın kimlik numarası delTc olarak kaydedildi.
        if not (self.hastaKontrol(delTc)):   #Kayıt silinmek istenirse çalışacak self parametresi.
            self.recordList.pop(delTc)  #self kullanıldı.
        else:
            print("Boyle bir kayit bulunamadi!")   #yukarıdaki blok çalışmaz ise ekrana kayıt bulunamadı ve tekrar kontrol edebilirisiniz yazdıdır. 
            print("Tekrar Kontrol Edebilirsiniz")

    def showAllRecords(self):   #Seçime göre showAllRecords fonksiyonu çalışır.
        pass
    def hastaKontrol(self, no):   #Seçime göre hasta kontrol fonksiyoru çalışır.
       pass


    @property   #Getter Setter metodu kullanılmaya çalışıldı.
    def recordList(self):
        

    @recordList.setter   #Getter Setter metodu kullanılmaya çalışıldı.
    def recordList(self, value):