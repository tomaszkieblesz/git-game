#Czy gałąź pro jest aktywna?
#from string import ascii_letters


sentencja=input()

sent=sentencja.lower()

ALFABET="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMęĘóÓłńŃŁŻŹćżźśŚ"

for x in sent:
    if x in (ALFABET):
        mfl="".join(x)
        print(mfl)








