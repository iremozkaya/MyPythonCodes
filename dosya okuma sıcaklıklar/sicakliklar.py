dosya_adi=r"C:\Users\LENOVO\OneDrive\Belgeler\dosya okuma sıcaklıklar\dosya_okuma_sicakliklar.txt"
bolgeler = {"ic Anadolu": [], "Marmara": [], "Ege": []}

with open(dosya_adi,"r") as dosya:
    for satir in dosya:
        satir=satir.strip()
        sehir,bolge,derece=satir.split("\\")
        derece=float(derece)

        if bolge in bolgeler:
            bolgeler[bolge].append((sehir,derece))

    en_sicak_derece=-1
    en_sicak_sehir=None
    

    for bolge,sehirler in bolgeler.items():
        print(f"{bolge} şehir sayısı: {len(sehirler)}")
        
        bolgedeki_sicak_sehir=sehirler[0]
        for sehir in sehirler:
            if sehir[1]>bolgedeki_sicak_sehir[1]:
                bolgedeki_sicak_sehir=sehir
        
        print(f"{bolge}daki en sıcak şehir: {bolgedeki_sicak_sehir[0]},{bolgedeki_sicak_sehir[1]}")

       

        if en_sicak_sehir is None or bolgedeki_sicak_sehir[1] > en_sicak_sehir[1]:
            en_sicak_sehir=bolgedeki_sicak_sehir
    print(f"en sıcak şehir: {en_sicak_sehir[0]},{en_sicak_sehir[1]}")