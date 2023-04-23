# импортируем библиотеку для создания графического интерфейса
import tkinter as tk

# создаем главное окно
root = tk.Tk()
root.title("Расчет свободного места на складе")

# создаем элементы интерфейса для ввода данных
cold_storage_label = tk.Label(root, text="Склад холода")
cold_storage_label.grid(row=0, column=0)

cold_storage_input = tk.Entry(root, width=10)
cold_storage_input.grid(row=1, column=0)

frozen_storage_label = tk.Label(root, text="Склад морозильного хранения")
frozen_storage_label.grid(row=0, column=1)

frozen_storage_input = tk.Entry(root, width=10)
frozen_storage_input.grid(row=1, column=1)

zone_label = tk.Label(root, text="Зона")
zone_label.grid(row=2, column=0)

zone_options = ["Подбор", "Хранение"]
zone_variable = tk.StringVar(root)
zone_variable.set(zone_options[0])

zone_dropdown = tk.OptionMenu(root, zone_variable, *zone_options)
zone_dropdown.grid(row=3, column=0)

# создаем функцию для расчета свободного места на складах
def calculate_free_space():
    # получаем значения из элементов интерфейса
    cold_storage_input_value = cold_storage_input.get()
    frozen_storage_input_value = frozen_storage_input.get()
    zone_value = zone_variable.get()

    # проверяем, что значения введены корректно
    try:
        cold_storage_input_value = int(cold_storage_input_value)
        frozen_storage_input_value = int(frozen_storage_input_value)
    except ValueError:
        error_label.config(text="Ошибка: введите целое число")
        return

    if cold_storage_input_value < 0 or frozen_storage_input_value < 0:
        error_label.config(text="Ошибка: введите положительное число")
        return

    # задаем вместимость складов и начальное количество занятых мест на складах
    cold_storage_capacity = 200
    frozen_storage_capacity = 150

    cold_storage_occupied = 0
    frozen_storage_occupied = 0

    # обновляем количество занятых мест на складах в соответствии с введенными данными
    cold_storage_occupied += cold_storage_input_value if zone_value == "Хранение" else 0
    frozen_storage_occupied += frozen_storage_input_value if zone_value == "Хранение" else 0

    cold_storage_occupied += cold_storage_input_value if zone_value == "Подбор" else 0
    frozen_storage_occupied += frozen_storage_input_value if zone_value == "Подбор" else 0

    # вычисляем количество свободных мест на складах
    cold_storage_free = cold_storage_capacity - cold_storage_occupied
    frozen_storage_free = frozen_storage_capacity - frozen_storage_occupied

    # обновляем текст меток с результатами расчета
    cold_storage_free_label.config(text="Количество свободных мест на складе холода:")
