kategoriler = {"Telefon": [], "Bilgisayar": [], "Kulaklık": []}
dosya_adi=r"C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\dosya okuma magaza\magaza.txt"
with open(dosya_adi,"r") as dosya:
    for satir in dosya:
        satir=satir.strip()
        marka,kategori,fiyat=satir.split("\\")
        fiyat=int(fiyat)

        if kategori in kategoriler:
            kategoriler[kategori].append((marka,fiyat))

    en_ucuz_fiyat=100000
    en_ucuz_urun_g=None
    for kategori,urun_listesi in kategoriler.items():
        sayi=len(kategoriler[kategori])
        print(f"{kategori} ürününden {sayi} adet satıldı.")
    
        for i in urun_listesi:
            if i[1]<en_ucuz_fiyat:
                en_ucuz_fiyat=i[1]
                k_en_ucuz_urun=i
        
        print(f"{kategori} kategorisindeki en ucuz ürün: {k_en_ucuz_urun[0]},{k_en_ucuz_urun[1]} TL")

        if en_ucuz_urun_g==None or k_en_ucuz_urun[1]<en_ucuz_urun_g[1]:
            en_ucuz_urun_g=k_en_ucuz_urun
        
    print(f"en ucuz ürün: {en_ucuz_urun_g[0]},{en_ucuz_urun_g[1]} TL")