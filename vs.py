adet=int(input())
liste1=[0]*adet
liste2=[0]*adet
liste3=[0]*adet
for i in range(adet):
    liste1[i]=int(input())
for i in range(adet):
    liste2[i]=int(input())
for i in range(adet):
    liste3[i]=liste1[i]*liste2[i]
for i in liste3:
    print(i, end=" ")
top=0
for i in liste3:
    top+=i
print()
print(f"{top/adet:.2f}")