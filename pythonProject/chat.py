print('text input')
a=input()
b1=a.find('h')
b2=a.find('e')
b3=a.find('ll')
b4=a.find('o')
a=a[b1]+a[b2]+a[b3:b4:3]+a[b4]
if a=="hello":
    print('yes')
else:print('no')







