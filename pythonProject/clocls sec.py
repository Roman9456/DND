print('введите кол-во')
n=int(input())
hours=(n//3600)%24
n=n%3600
minutes=n//60
n=n%60
secundes=n
print(hours,':',minutes//10, minutes%10,':', secundes//10,secundes%10, sep='')
