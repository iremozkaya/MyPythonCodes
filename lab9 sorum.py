#lab9 sorum
class Devices:
    def __init__(self,ad,tip,sarj,durum="OFF"):
        self.ad=ad
        self.tip=tip
        self.sarj=sarj
        self.durum=durum
    dusuk_batarya_listesi=[]

    def dusuk_batarya(self,esikdeger):
        if self.sarj<esikdeger:
            self.dusuk_batarya_listesi.append(self.ad)
        if len(self.dusuk_batarya_listesi)==0:
            print("no devices")
        return
    def ac(self,durum):
        if durum=="ON":
            print("already ON")
        else:
            durum="ON"
            print("acildi") 
    def kapat(self,durum):
        if durum=="OFF":
            print("already OFF")
        else:
            durum="OFF"
            print("kapatildi")
    
    def sarjet(self,miktar):
        if miktar<0:
            print("negative value")
        else:
            self.sarj+=miktar
            print("charged")
        
    def bilgial(self):
        print(f"name:{self.ad} type:{self.tip}, battery:{self.sarj} status: {self.durum}")


cihaz_sayisi=int(input())
for i in range(cihaz_sayisi):

    ad=input()
    tip=input()
    sarj=int(input())
    durum="OFF"
sistem=Devices(ad,tip,sarj)
for i in range(cihaz_sayisi):

    islem=int(input())
    if islem==1:
        esikdeger=int(input())
    sistem.dusuk_batarya(esikdeger)
    elif islem==2:
        islem=int(input())
        if islem==1:
            sistem.ac(durum)
        if islem==2:
            sistem.kapat(durum)
        if islem==3:
            miktar=int(input())
            sistem.sarjet(miktar)
        if islem==4:
            sistem.bilgial()
        else:
            print("invalid choice")
    elif islem==-1:
        print("exit")
        break
    else:
        print("invalid choice")

    
