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
        pass

    def yeniKayit(self):
        pass

    def hastalikSecimi(self):
        pass

    def logOut(self):
        print("Oturum kapatiliyor!! Gule gule")
        self.oturumAcma = False

