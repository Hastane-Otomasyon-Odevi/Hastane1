class Patient():
    def __init__(self,tc,soyisim):        #Split
        self.Tc = tc
        self.soyisim = soyisim
    
    def __str__(self):
        return "Hasta tc :{}\nHasta soyisim :{}".format(self.Tc,self.soyisim)