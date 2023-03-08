x = int(input())
y = int(input())
z = int(input())
n = int(input())
x_list=[i for i in range(x+1)]
y_list=[i for i in range(y+1)]
z_list=[i for i in range(z+1)]
ijk=[]
for i in x_list:
    for j in y_list:
        for k in z_list:
            ijk.append([i,j,k])
sonuc=[]          
for i in ijk:
    summation=sum(i)
    if summation==n:
        continue
    else:
        sonuc.append(i)
print(sonuc)
