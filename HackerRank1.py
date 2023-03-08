harfler=[]
liste=[]
sayilar=[int(x) for x in input().split()]

for _ in range(sayilar[0]):
    liste.append(input())
for _ in range(sayilar[2]):
    harfler.append(input())
for i in range(len(harfler)):
    sonuc=[]
    for k in range(len(liste)):
        if harfler[i]==liste[k]:
            sonuc.append(k+1)
        else:
            continue
    if len(sonuc)==0:
        sonuc.append(-1)
        print(*sonuc)
    else:
        print(*sonuc)
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem