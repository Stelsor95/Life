import random

# Словарь для хранения игрушек и их весов
toys = {}

# Функция для добавления новой игрушки


def add_toys():
    title = input("Введите название игрушки: ")
    weight = float(input("Введите вес игрушки (в килограммах): "))
    toys[title] = weight
    print(f"Игрушка '{title}' с весом {weight} кг успешно добавлена!")

# Функция для случайного выбора игрушек


def select_toys():
    summa_weights = sum(toys.values())
    random_number = random.uniform(0, summa_weights)

    the_current_sum = 0
    for title, weight in toys.items():
        the_current_sum += weight
        if the_current_sum >= random_number:
            return title


# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить новую игрушку")
    print("2. Выбрать игрушку")
    print("3. Выйти из программы")

    choice = input("Введите номер действия (1/2/3): ")

    if choice == '1':
        add_toys()
    elif choice == '2':
        if not toys:
            print("Сначала добавьте игрушки.")
        else:
            selected_toys = select_toys()
            print(f"Вы выбрали игрушку: {selected_toys}")
    elif choice == '3':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите правильное действие.")
