def func(n):
    if n==1:
        return n
    return str(func(n-1))+str(n)
print(func(int(input())))