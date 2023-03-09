x=int(input())
liste=[]
for _ in range(x):
    inp=input().split()
    
    if inp[0]=='insert':
        liste.insert(int(inp[1]),int(inp[2]))
    elif inp[0]=='print':
        print(liste)
    elif inp[0]=='remove':
        liste.remove(int(inp[1]))
    elif inp[0]=='append':
        liste.append(int(inp[1]))
    elif inp[0]=='sort':
        liste.sort()
    elif inp[0]=='pop':
        liste.pop(-1)
    elif inp[0]=='reverse':
        liste.reverse()