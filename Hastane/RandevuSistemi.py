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
            if choose == 1 and (not self.oturumAcma): # kullanıcı 1 girdisi girerse oturum açma işlemi çalışır.
                self.giris()
            if choose == 2:                           # kullanıcı 2 girdisi girerse yeni kayıt açma işlemi çalışır.
                self.yeniKayit()
            if choose == 3:                           # kullancı 3 girdisi girerse hastalık secimi işlemi çalışır.
                self.hastalikSecimi()
            if choose == 4:                           # kullanıcı 4 girdisi girerse gecmis olsun yazısı çalışır.
                print("Gecmis olsun")
                cycle = False
            if choose == 5:                           # kullanıcı 5 girdisi girerse tüm kayıtları gösterir.
                self.kayit.showAllRecords()
            if choose == 6:                           # kullanıcı 6 girdisi girerse oluşturulan kayıt silinir.
                self.kayit.kayitSil()

            print()

    def giris(self):
        pass

    def yeniKayit(self):
        pass

    def hastalikSecimi(self):
        pass

    def logOut(self):
        print("Oturum kapatiliyor!! Gule gule")
        self.oturumAcma = False

    def guncel(self):
        pass