sentencja=input("Wpisz zdanie i naciśnij ENTER:")

sent=sentencja.lower().strip()

ALFABET="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMąĄęĘóÓłńŃŁŻŹćżźśŚ"

mlf=[]
for x in sent:
    if x in (ALFABET):
        mlf.append(x)
#print(mlf)
baza=[]

alfa=[]
for i in range(mlf.__len__()):
    l=mlf[i]
    litery=mlf.count(l)
    if [litery, l] not in baza:
        baza.append([litery,l])

srt=sorted(baza)
#print(srt)
#print(srt[-1])
if srt[-1][0]==srt[-2][0]:
    a=mlf.index(srt[-1][1])
    b=mlf.index(srt[-2][1])
    y=min(a,b)
    #print(y)
    print("Najliczniej występującą literą w tekście jest: "+sent[y])
else:
    print("Najliczniej występującą literą w tekście jest: "+srt[-1][1])






