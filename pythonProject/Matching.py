boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort(),girls.sort()
if len(boys) != len(girls):
    print ("Кол-во представителей обоих полов - отчличаются, кто то может остаться без пары")
else:
    for b, g in zip(boys, girls):
        print(f"{b}: and {g}")