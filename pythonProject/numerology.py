courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
	 "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан",
	 "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов",
	 "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен",
	 "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев",
	 "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
	 "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
	 "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

codes_info = [
	"",
	"1 — число цели, которая проявляется в форме агрессивности и амбиций",
	"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
	"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
	"4 — означает устойчивость и прочность",
	"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
	"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
	"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
	"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
	"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
]
# Здесь ничего менять не нужно, это готовый код, который считает число имени
def calc_namecode(name):
	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
			   "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

	name = name.upper()
	code = 0
	for letter in name:
		try:
			ltr_code = letters.index(letter) % 9
		except:
			continue
		if ltr_code == 0:
			ltr_code = 9
		code += ltr_code

	while code > 9:
		curr = code // 10 + code % 10
		code = curr

	return code

# Добавьте сюда ваш код из Задачи 1
all_list = []
for m in mentors:
    all_list.extend(m)

all_names_list = []
for mentor in all_list:
    name = mentor.split()[0]
    all_names_list.append(name)


# уникальные имена будут в unique_names
unique_names = set(all_names_list)



# Этот код создаст вам уже готовый (пока что пустой) список, в который вы будете добавлять имена
names_codes = [[] for n in range(10)]

# Подсказка: в список names_codes дописывайте список имён с группировкой по числу имени.
# Рекомендуем для простоты список с именами записывать по индексу, который равняется числу имени
# Например, код имени Владимир — 2, и итоговый результат был бы
# names_codes = [[], [], ["Владимир"]] - внутренний список с именем Владимир находится по индексу 2 в списке names_codes
# Самый первый список с индексом 0 будет всегда пустым, т. к. нет числа имени 0

# Перебираем все имена и группируем их по числу имени
for name in unique_names:
	# Команду ниже используйте как есть - она вычисляет число имени. На входе функция принимает имя (регистр не важен)
	# На выходе возвращает целое число от 1 до 9 - это число имени. Например, если введёте "Анна" - получите 5
	code = calc_namecode(name)

	# Допишите код, который добавит ещё одно имя к нужному числу имени в списке names_codes
	names_codes[code].append(name)

# Выводим окончательный результат на экран
for id, _ in enumerate(names_codes):
	if id==0:
		continue
	# Допишите вывод расшифровки числа имени из codes_info
	# Должно выводиться так: 1 — число цели, которая проявляется в форме агрессивности и амбиций
	print(codes_info[id])

	# Теперь нужно отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
	# Допишите код ниже:
	all_names_sorted = sorted(list(names_codes[id]))

	# Допишите код, который выводит сообщение на экран
	# Должно выводиться так: Коду 1 соответствуют: Азамат, Денис, Роман, Ринат, Евгений, Адилет, Сергей
	print(f"Коду {id} соответствуют: {', '.join(all_names_sorted)}")