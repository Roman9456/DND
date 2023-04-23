print('введите месяц рождения').lower()
mounth=input().lower()
print('Введите день рождения')
day=int(input())
if mounth ==    'март' and day<=31 and day>=21 or mounth=='апрель' and day<=19:
    print("По гороскопу вы Овен")
elif mounth == 'апрель' and day<=30 and day>=21 or mounth=='май' and day<=21:
    print("По гороскопу вы Телец")
elif mounth =='май' and day<=30 and day>=22 or mounth == 'июнь' and day <= 21:
    print("По гороскопу вы Близнецы")
elif mounth == 'июнь' and day <= 30 and day >= 22 or mounth == 'июль' and day <= 22:
    print("По гороскопу вы Рак")
elif mounth == 'июль' and day <= 30 and day >= 23 or mounth=='август' and day<=21:
    print("По гороскопу вы Лев")
elif mounth == 'август' and day <= 30 and day >= 22 or mounth == 'сентябрь' and day <= 23:
    print("По гороскопу вы Дева")
elif mounth == 'сентябрь' and day <= 30 and day >= 24 or mounth == 'октябрь' and day <= 23:
    print("По гороскопу вы Весы")
elif mounth == 'октябрь' and day <= 30 and day >= 24 or mounth == 'ноябрь' and day <= 22:
    print("По гороскопу вы Скорпион")
elif mounth == 'ноябрь' and day <= 30 and day >= 23 or mounth == 'декабрь' and day <= 22:
    print("По гороскопу вы Стрелец")
elif mounth == 'декабрь' and day <= 30 and day >= 23 or mounth == 'январь' and day <= 20:
    print("По гороскопу вы Козерог")
elif mounth == 'январь' and day <= 30 and day >= 21 or mounth == 'февраль' and day <= 19:
    print("По гороскопу вы Водолей")
else:print("По гороскопу вы Рыбы")








