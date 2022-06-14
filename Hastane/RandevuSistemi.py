from numpy import choose

import pandas as pd # awesome python kutuphanesi zorunlu oldugu icin pandasi kullandik.
from hastane import Hastane # menu ve hastandeki verileri cekebilmek icin birlikte kullandik.

class GirisEkrani():   #giris ekrani olusturmak icin bir class tanimladik.
    def __init__(self):
        print("Randevu sistemine hos geldiniz")
        self.oturumAcma = False #acildgi gibi calismamasi icin false olarak atandi
        self.cycle = True
        self.kayit = Hastane()
        self. doctors = ["Hakan Tasiyan", "Muslum Gurses", "Esengul", "Bergen","Azer Bulbul"]  #self ile dokorlar tanımlandı
        self.disease = ["Agiz Dis Cene Cerrahisi", "Deri ve Zuhrevi", "Goz hastaliklari", "Noroloji","Kalp Hastalıkları"] #self ile hastaıklar tanımlandı.
        self.vaccine = ["Turcovac","Biontech","Sinovac","Moderna"]  #self ile aşılar tanımlandı.
        
        self.doctorsDisease = {"Diseases": self.disease, "Doctors": self.doctors} #self ile doktorlar ve hastalar eşleştirildi.


    def randevuAl(self):
        while self.cycle: # while dongusune girebilmesi icin True olarak atama yaptik.
            if self.oturumAcma == False: #cycle atadigimiz degerden dolayi while dongusune dondu.
                print("Giris yapmak icin : 1") # giris yapmak icin 1 rakamina basilir.
                print("Kayit olmak icin : 2")  # kayit olmak icin 2 rakamina basilir.
            print("Randevu almak icin : 3") # randevu almak icin 3 rakamina basilir.
            print("Logout icin : 4")       # hasta oturumunu sonlandirmak icin 4 rakamina basilir.
            print("Cikmak icin : 5")       # cikis yapmak icin 5 rakamina basilir.
            print("Bizi seçtiginiz icin tesekkürler")  # ekrana kucuk bir bilgilendirme notu ekledik.
            print()
            choose = int(input("Yapmak istediginiz islem :  ")) # yapmak istedigi islemi secmek icin input ve choose'a kayit aldik.

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
                self.cycle = False
            if choose == 5:                           # kullanici 5 girdisi girerse tum kayitlari gosterir.
                self.cycle = False
            if choose == 6:                           # kullanici 6 girdisi girerse olusturulan kayit silinir.
                self.kayit.kayitSil()

            print()

    def giris(self): # giris ekraninin calismasi icin ggiris fonksiyonu calistirildi.
        user = input("Hastanin tc'sini giriniz: ").strip()          # Guvenlik kontrolune gerek yok
        password = input("Hastanin soyismini giriniz: ").strip()    # Guvenlik kontrolune gerek yok

        if user in self.kayit.recordList.keys():
            if password == self.kayit.recordList[user]:
                print("Sisteme basariyla giris yapildi!")
                self.oturumAcma = True
            else:
                print("Sifre yanlis girildi!!")
        else:
            print("Bu kayitta bir kullanici bulunamadi!")
        print()

    def yeniKayit(self): # yeni kayit ekraninin calismasi icin yeni kayit fonksiyonu calistirildi.
        self.kayit.hastaKayit()
    def hastalikSecimi(self): # hastalik secimi ekraninin  ccalismasi icin hastalik secimi fonksiyonu calistirildi. 
        if self.oturumAcma == True: # kod bloğunun çalışması için oturumacma True olarak atandı
            print("Doktor randevusu mu asi randevusu mu?")
            choose = input("Asi icin : 1\nDoktor randevusu icin : 2\nSeçiminizi Giriniz : ").strip() # input ile kullanıcıdan veri alındı .strip() ile düzenleme yapıldı
            while not choose.isnumeric(): # döngüye girebilmesi için sadece numaradan oluşması şartı kullanıldı
                choose = input("Gecerli formatta bir secim giriniz: ")
            if choose == '2':
                print("\nHastalik ve Listesi : \n")
                df = pd.DataFrame.from_dict(self.doctorsDisease) # awesome python kütüphanesi pandas ile doktor hastalık eşleştirmesi yapılmaya çalışıldı
                print(df.to_string()) # pandas ile veriyi string e çevirdim
                secim = input("\nSecmek istediginiz hastaligin kodunu girin: ").strip() # input ile kullanıcıdan veri alındı .strip() ile düzenleme yapıldı
                while not secim.isnumeric() or int(secim) < 0 or int(secim) > 4:
                    secim = input("Alan kodu en soldaki sutundaki sayisal degerlerdir tekrar deneyiniz: "),
                print("Randevu bilgileri : ")
                df_1 = df.iloc[int(secim)] 
                print(df_1.to_string())
                print("\nRandevunuz basariyla olusturuldu! Gecmis olsun.")
                self.cycle = False

            if choose == '1':
                print()
                sr = pd.Series(self.vaccine)
                print(sr.to_string(),end='\n')
                secim = input("\nSecmek istediginiz asinin kodunu girin: ").strip()
                while not secim.isnumeric() or int(secim) < 0 or int(secim) > 3:
                    secim = input("Alan kodu en soldaki sutundaki sayisal degerlerdir tekrar deneyiniz: "),
                sr2 = sr.iloc[int(secim)]
                print("Randevu bilgileri : ")
                print(sr2)
                self.cycle = False
                print("\nRandevunuz basariyla olusturuldu! Gecmis olsun.")
        else:
            print("Islem yapmadan once oturum aciniz!!")


    def logOut(self):
        print("Oturum kapatiliyor!! Gule gule") # logOut(cikis) ekraninin  calismasi icin logOut fonksiyonu calistirildi.
        self.oturumAcma = False # Sistemin kapatılması için oturumacma False olarak atanıyor