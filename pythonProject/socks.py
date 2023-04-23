import math
print('введите в строчку кол-во карсных и кол-во синих носков')
a,b=map(int,input().split())
c=min(a,b)
x=(a+b)/2-c
print(math.floor(c),math.floor(x))
