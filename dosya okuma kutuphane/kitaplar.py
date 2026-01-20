kutuphane = {"Roman": [], "Bilim Kurgu": [], "Tarih": []}
dosya_adi=r"C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\dosya okuma kutuphane\kitaplar.txt"
with open(dosya_adi,"r") as dosya:
    for satir in dosya:
        satir=satir.strip()
        ad,tur,sayfa=satir.split("\\")
        sayfa=int(sayfa)
        if tur in kutuphane:
            kutuphane[tur].append((ad,sayfa))
    
    en_kalin_sayfa=0
    ince_kitaplar=[]


    for tur,kitaplar in kutuphane.items():
        tur_kalin_kitap=None
        tur_en_kalin_sayfa=0
        top_sayfa=0
        for kitap in kitaplar:
            top_sayfa+=kitap[1]
            if kitap[1]<400:
                ince_kitaplar.append(kitap)
            if kitap[1]>tur_en_kalin_sayfa:
                tur_en_kalin_sayfa=kitap[1]
                tur_kalin_kitap=kitap
        print(f"{tur} türünde toplam {top_sayfa} sayfa var.")
        
        if tur_kalin_kitap==None:
            print("None")
        else:
            print(f"{tur} türünün en kalın kitabı: {tur_kalin_kitap[0]}-->{tur_kalin_kitap[1]} sayfa.")

    if tur_en_kalin_sayfa>en_kalin_sayfa:
        en_kalin_sayfa=tur_en_kalin_sayfa
        en_kalin_kitap=tur_kalin_kitap
        print(f"en kalın kitap: {tur_kalin_kitap[0]}-->{tur_kalin_kitap[1]}")
    
    for i in ince_kitaplar:
        print(i[0],i[1])