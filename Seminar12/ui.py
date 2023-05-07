from logger import input_data, print_data, update_data, delete_data


def command():
    inp = int(input("Добрый день! Ты в специальном боте! Выбери число - вариант для дальнейшей работы (1-2-3-4): "
                    "\n1 -> Запись данных"
                    "\n2 -> Выборка данных"
                    "\n3 -> Редактирование данных"
                    "\n4 -> Удаление данных"
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
