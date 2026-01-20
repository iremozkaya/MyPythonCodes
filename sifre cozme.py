muh_1={'L': 'A', 'U': 'B', 'A': 'C', 'P': 'D', 'I': 'E', 'M': 'F', 'T': 'G', 'K': 'H', 'O': 'I', 'V': 'J', 'H': 'K', 'G': 'L', 'C': 'M', 'Z': 'N', 'B': 'O', 'S': 'P', 'F': 'Q', 'J': 'R', 'R': 'S', 'N': 'T', 'E': 'U', 'X': 'V', 'D': 'W', 'Y': 'X', 'Q': 'Y', 'W': 'Z'}
muh_2={'J': 'A', 'H': 'B', 'U': 'C', 'K': 'D', 'C': 'E', 'O': 'F', 'L': 'G', 'X': 'H', 'S': 'I', 'R': 'J', 'F': 'K', 'V': 'L', 'Q': 'M', 'A': 'N', 'M': 'O', 'B': 'P', 'Z': 'Q', 'P': 'R', 'E': 'S', 'W': 'T', 'D': 'U', 'T': 'V', 'N': 'W', 'Y': 'X', 'I': 'Y', 'G': 'Z'}

def ceviri(sozluk,kelime):
    cevrilmis_harfler=[]
    kelime=kelime.strip().upper()
    for i in kelime:
        if i in sozluk:
            cevrilmis_harfler.append(sozluk[i])
        else:
            cevrilmis_harfler.append("*")
    for i in cevrilmis_harfler:
        print(i,end="")
    print()
    return cevrilmis_harfler

hak=5
for i in range(5):
    muh1=input()
    muh2=input()
    
    
    cozum1=ceviri(muh_1,muh1)

    
    cozum2=ceviri(muh_2,muh2)

    if cozum1==cozum2:
        for i in cozum1:
            print(i,end="")
        print()
        print("SUNUCU AKTİFFFF")
        break
    else:
        print("hatali sifre")
        hak-=1
    print(hak)
    if hak==0:
        print("sistem kilitlendi :(")
        break
