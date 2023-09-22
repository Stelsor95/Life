# Создаем пустой словарь для хранения заметок
notes = {}

# Функция для создания новой заметки


def create_a_tag():
    heading = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    notes[heading] = text
    print("Заметка успешно создана!")

# Функция для сохранения заметок в файл


def save_references():
    with open("заметки.txt", "w") as file:
        for heading, text in notes.items():
            file.write(f"{heading}:\n{text}\n\n")
    print("Заметки сохранены в файле 'заметки.txt'.")

# Функция для чтения списка заметок из файла


def read_references():
    try:
        with open("заметки.txt", "r") as file:
            print("Список заметок:")
            print(file.read())
    except FileNotFoundError:
        print("Файл 'заметки.txt' не найден. Создайте заметку сначала.")

# Функция для редактирования существующей заметки


def edit_a_note():
    heading = input("Введите заголовок заметки для редактирования: ")
    if heading in notes:
        new_text = input("Введите новый текст заметки: ")
        notes[heading] = new_text
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с таким заголовком не найдена.")

# Функция для удаления заметки


def delete_a_note():
    heading = input("Введите заголовок заметки для удаления: ")
    if heading in notes:
        del notes[heading]
        print("Заметка успешно удалена!")
    else:
        print("Заметка с таким заголовком не найдена.")


# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Создать новую заметку")
    print("2. Сохранить заметки в файл")
    print("3. Прочитать список заметок")
    print("4. Редактировать существующую заметку")
    print("5. Удалить заметку")
    print("6. Выйти из программы")

    choice = input("Введите номер действия (1/2/3/4/5/6): ")

    if choice == '1':
        create_a_tag()
    elif choice == '2':
        save_references()
    elif choice == '3':
        read_references()
    elif choice == '4':
        edit_a_note()
    elif choice == '5':
        delete_a_note()
    elif choice == '6':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите правильное действие.")
