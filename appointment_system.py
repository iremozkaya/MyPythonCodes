ilce={'J': 'A', 'H': 'B', 'U': 'C', 'K': 'D', 'C': 'E', 'O': 'F', 'L': 'G', 'X': 'H', 'S': 'I', 'R': 'J', 'F': 'K', 'V': 'L', 'Q': 'M', 'A': 'N', 'M': 'O', 'B': 'P', 'Z': 'Q', 'P': 'R', 'E': 'S', 'W': 'T', 'D': 'U', 'T': 'V', 'N': 'W', 'Y': 'X', 'I': 'Y', 'G': 'Z'}
sehir={'L': 'A', 'U': 'B', 'A': 'C', 'P': 'D', 'I': 'E', 'M': 'F', 'T': 'G', 'K': 'H', 'O': 'I', 'V': 'J', 'H': 'K', 'G': 'L', 'C': 'M', 'Z': 'N', 'B': 'O', 'S': 'P', 'F': 'Q', 'J': 'R', 'R': 'S', 'N': 'T', 'E': 'U', 'X': 'V', 'D': 'W', 'Y': 'X', 'Q': 'Y', 'W': 'Z'}
sokakno_inissay={0:6,1:5,2:4,3:7,4:1,5:2,6:0,7:3,8:9,9:8}


def ceviri_str(sozluk,kelime):
    cevrilmis_kelime=[]
    for i in kelime:
        cevrilmis_harf=sozluk[i]
        cevrilmis_kelime.append(cevrilmis_harf)
    return cevrilmis_kelime

def ceviri_int(sozluk,sayilar):
    cevrilmis_sayilar=[]
    for i in str(sayilar):
        cevrilmis_sayi=sozluk[int(i)]
        cevrilmis_sayilar.append(cevrilmis_sayi)
    return cevrilmis_sayilar

inis_sayisi=int(input())
inis_cevrilmis=ceviri_int(sokakno_inissay,inis_sayisi)

for i in range(inis_cevrilmis[0]):
    g_sehir=input()
    if len(g_sehir)>=3 and len(g_sehir)<=10:
        sehrimiz=ceviri_str(sehir,g_sehir)
    else:
        print("ucuslar iptal.")
        break

    g_ilce=input()
    ilcemiz=ceviri_str(ilce,g_ilce)
    
    g_sokak=input()
    if len(g_sokak)==4:
        sokak=ceviri_int(sokakno_inissay,g_sokak)
    else:
        print("ucuslar iptal.")
        break
        
    for j in sehrimiz:
        print(j,end="")
    print()

    for k in ilcemiz:
        print(k,end="")
    print()

    for m in sokak:
        print(m,end="")
    print()
    

        
    

