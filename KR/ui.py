from logger import input_data, print_data, update_data, delete_data


def command():
    inp = int(input("Это консольное приложение для создания заметок! Выбери число - вариант для дальнейшей работы (1-2-3-4): "
                    "\n1 -> Создание заметки"
                    "\n2 -> Выбор заметки"
                    "\n3 -> Редактирование заметки"
                    "\n4 -> Удаление заметки"
                    "\nВыбор -> "))
    if inp == 1:
        input_data()
    elif inp == 2:
        print_data()
    elif inp == 3:
        update_data()
    elif inp == 4:
        delete_data()
    else:
        print("Данные введены некорректно!!!")
        command()
