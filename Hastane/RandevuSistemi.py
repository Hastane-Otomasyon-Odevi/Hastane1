import pandas as pd

from Menu import Hastane

class GirisEkrani():
    def __init__(self):
        print("Randevu sistemine hos geldiniz")
        self.oturumAcma = False
        self.kayit = Hastane()
        self. doctors = ["Hakan Tasiyan", "Muslum Gurses", "Esengul", "Bergen"]
        self.disease = ["Agiz Dis Cene Cerrahisi", "Deri ve Zuhrevi", "Goz hastaliklari", "Noroloji"]

        self.doctorsDisease = {"Diseases": self.disease, "Doctors": self.doctors}

    def randevuAl(self):
        cycle = True
        while cycle:
            print("Giris yapmak icin : 1")
            print("Kayit olmak icin : 2")
            print("Randevu almak icin : 3")
            print("Logout icin : 4")
            print("Cikmak icin : 5")
            print()
            choose = int(input("Yapmak istediginiz islem :  "))

            if self.oturumAcma == True and choose == 1:
                print("Yeni bir oturum acmadan once oturumunuzu kapatiniz.")
            if choose == 1 and (not self.oturumAcma):
                self.giris()
            if choose == 2:
                self.yeniKayit()
            if choose == 3:
                self.hastalikSecimi()
            if choose == 4:
                print("Gecmis olsun")
                cycle = False
            if choose == 5:
                self.kayit.showAllRecords()
            if choose == 6:
                self.kayit.kayitSil()

            print()

    def giris(self):
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


    def yeniKayit(self):
        self.kayit.hastaKayit()

    def hastalikSecimi(self):
        if self.oturumAcma == True:
            print("\nHastalik ve Listesi : \n")
            df = pd.DataFrame.from_dict(self.doctorsDisease)
            print(df.to_string())
            secim = input("\nSecmek istediginiz hastaligin kodunu girin: ").strip()
            while not secim.isnumeric() or int(secim) < 0 or int(secim) > 4:
                secim = input("Alan kodu en soldaki sutundaki sayisal degerlerdir tekrar deneyiniz: "),
            print("Randevu bilgileri : ")
            df_1 = df.iloc[int(secim)]
            print(df_1.to_string())
            print("\nRandevunuz basariyla olusturuldu! Gecmis olsun.")
        else:
            print("Islem yapmadan once oturum aciniz!!")


    def logOut(self):
        print("Oturum kapatiliyor!! Gule gule")
        self.oturumAcma = False

