import pandas as pd # awesome python kutuphanesi zorunlu oldugu icin pandasi kullandik.
from hastane import Hastane # menu ve hastandeki verileri cekebilmek icin birlikte kullandik.

class GirisEkrani():   #giris ekrani olusturmak icin bir class tanimladik.
    def __init__(self):
        print("Randevu sistemine hos geldiniz")
        self.oturumAcma = False #acildgi gibi calismamasi icin false olarak atandi
        self.kayit = Hastane()

    def randevuAl(self):
        cycle = True # while dongusune girebilmesi icin True olarak atama yaptik.
        while cycle: #cycle atadigimiz degerden dolayi while dongusune dondu.
            print("Giris yapmak icin : 1") # giriş yapmak için 1 rakamına basılır.
            print("Kayit olmak icin : 2")  # kayıt olmak için 2 rakamına basılır.
            print("Randevu almak icin : 3")# randevu almak için 3 rakamına basılır.
            print("Logout icin : 4")       # hasta oturumunu sonlandırmak için 4 rakamına basılır
            print("Cikmak icin : 5")       # çıkış yapmak için 5 rakamına basılır.
            print("Bizi seçtiginiz icin tesekkürler")  # ekrana küçük bir bilgilendirme notu ekledik.
            choose = int(input("Yapmak istediginiz islem :  ")) # yapmak istediği işlemi seçmek için input ve choose'a kayıt aldık.

            if self.oturumAcma == True and choose == 1:
                print("Yeni bir oturum acmadan once oturumunuzu kapatiniz.")
            if choose == 1 and (not self.oturumAcma): # kullanici  1 girdisi girerse oturum acma islemi calisir.
                self.giris()
            if choose == 2:                           # kullanici 2 girdisi girerse yeni kayit acma islemi calisir.
                self.yeniKayit()
            if choose == 3:                           # kullanci 3 girdisi girerse hastalik secimi islemi calisir.
                self.hastalikSecimi()
            if choose == 4:                           # kullanici 4 girdisi girerse gecmis olsun yazisi calisir..
                print("Gecmis olsun")
                cycle = False
            if choose == 5:                           # kullanici 5 girdisi girerse tum kayitlari gosterir.
                self.kayit.showAllRecords()
            if choose == 6:                           # kullanici 6 girdisi girerse olusturulan kayit silinir.
                self.kayit.kayitSil()

            print()

    def giris(self): # giris eekraninin calismasi icin ggiris fonksiyonu calistirildi.
        pass

    def yeniKayit(self): # yeni kayit ekraninin calismasi icin yeni kayit fonksiyonu calistirildi.
        pass

    def hastalikSecimi(self): # hastalik secimi ekraninin  ccalismasi icin hastalik secimi fonksiyonu calistirildi. 
        pass

    def logOut(self):
        print("Oturum kapatiliyor!! Gule gule") # logOut(cikis) ekraninin  calismasi icin logOut fonksiyonu calistirildi.
        self.oturumAcma = False

    def guncel(self):
        pass