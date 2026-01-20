yonetmenler={"Nolan":[],"James Cameron":[]}
dosya_adi=r"C:\Users\LENOVO\Downloads\h11\örnek3\filmler.txt"


with open(dosya_adi,"r") as dosya:
    for i in dosya:
        i=i.strip()
        film,yonetmen,puan=i.split("\\")
        puan=float(puan)

        if yonetmen in yonetmenler:
            yonetmenler[yonetmen].append((film,puan))

    

en_iyi_puan=-1
for yonetmen,filmler in yonetmenler.items():
    print(f"yonetmen: {yonetmen}")
    print(f"film sayısı: {len(filmler)}")

    yonetmenin_en_iyisi=filmler[0]

    for i in filmler:
        if i[1]>yonetmenin_en_iyisi[1]:
            yonetmenin_en_iyisi=i
             
    print(f"yonetmenin en iyi filmi: {yonetmenin_en_iyisi[0]},{yonetmenin_en_iyisi[1]}")

    if yonetmenin_en_iyisi[1]>en_iyi_puan:
        en_iyi_puan=yonetmenin_en_iyisi[1]
        en_iyi_film=yonetmenin_en_iyisi
    
print(f"en iyi film: {en_iyi_film[0]},{en_iyi_film[1]}")
