from other_functions import clear_file
from data_create import get_name_data, get_surname_data, get_address_data, get_phone_data


def input_data():
    name = get_name_data()
    surname = get_surname_data()
    phone = get_phone_data()
    address = get_phone_data()
    inp = int(input("В каком формате записать данные!"
                    f"\nВыбери число - вариант для записи (1/2):"
                    f"\n1 -> Запись в столбец:"
                    f"\n{name}"
                    f"\n{surname}"
                    f"\n{phone}"
                    f"\n{address}"
                    f"\n2 -> Запись в строку:"
                    f"\n{name}; {surname}; {phone}; {address}"
                    "\nВыберите вариант -> "))
    while inp != 1 and inp != 2:
        print("Некорректно введены данные")
        inp = int(input("Выбери число - вариант для записи (1/2)"
                        "\nВыберите вариант -> "))
    if inp == 1:

        with open("first.csv", 'a', encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif inp == 2:
        with open("second.csv", 'a', encoding="utf-8") as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("first.csv", 'r', encoding="utf-8") as f:
        first = f.readlines()
        first_list = []
        j = 0
        for i in range(len(first)):
            if first[i] == '\n' or i == len(first) - 1:
                first_list.append(''.join(first[j:i + 1]))
                j = i
        print("".join(first_list))

    print("Вывожу данные из 2 файла: \n")
    with open("second.csv", 'r', encoding="utf-8") as f:
        second = f.readlines()
        print(second)


def update_data():
    inp = int(input("В каком файле требуется редактирование данных?"
                    f"\nВыбери число - вариант для выбора файла (1 - first.csv / 2 - second.csv):"
                    "\nВыберите вариант -> "))
    while inp != 1 and inp != 2:
        print("Некорректно введены данные")
        inp = int(input("Выбери число - вариант для выбора файла (1 - first.csv / 2 - second.csv):"))
    if inp == 1:
        inp_index = int(input("Введите номер записи для редактирования -> "))
        with open("first.csv", 'r', encoding="utf-8") as f:
            first = f.readlines()
            first_dict = {}
            j = 0
            key = 1
            for i in range(len(first)):
                if first[i] == '\n' or i == len(first) - 1:
                    value = ''.join(first[j:i + 1])
                    first_dict[key] = value
                    j = i + 1
                    key += 1
            if inp_index in first_dict.keys():
                name_update = get_name_data()
                surname_update = get_surname_data()
                phone_update = get_phone_data()
                address_update = get_address_data()
                first_dict[inp_index] = f"{name_update}\n{surname_update}\n{phone_update}\n{address_update}\n\n"
                clear_file("first.csv")
                with open("first.csv", 'a', encoding="utf-8") as f:
                    for key in first_dict.keys():
                        f.write(first_dict[key])
            else:
                update_data()

    elif inp == 2:
        inp_index = int(input("Введите номер записи для редактирования -> "))
        with open("second.csv", 'r', encoding="utf-8") as f:
            second = f.readlines()
            second_dict = {}
            key = 1
            for i in range(len(second)):
                if second[i] != '\n':
                    second_dict[key] = second[i] + '\n'
                    key += 1
            if inp_index in second_dict.keys():
                name_update = get_name_data()
                surname_update = get_surname_data()
                phone_update = get_phone_data()
                address_update = get_phone_data()
                second_dict[inp_index] = f"{name_update}; {surname_update}; {phone_update}; {address_update}\n\n"
                clear_file("second.csv")
                with open("second.csv", 'a', encoding="utf-8") as f:
                    for key in second_dict.keys():
                        f.write(second_dict[key])
            else:
                update_data()


def delete_data():
    inp = int(input("В каком файле требуется удалить запись?"
                    f"\nВыбери число - вариант для выбора файла (1 - first.csv / 2 - second.csv):"
                    "\nВыберите вариант -> "))
    while inp != 1 and inp != 2:
        print("Некорректно введены данные")
        inp = int(input("Выбери число - вариант для выбора файла (1 - first.csv / 2 - second.csv):"))
    if inp == 1:
        inp_index = int(input("Введите номер записи для удаления -> "))
        with open("first.csv", 'r', encoding="utf-8") as f:
            first = f.readlines()
            first_dict = {}
            j = 0
            key = 1
            for i in range(len(first)):
                if first[i] == '\n' or i == len(first) and first[i] != "":
                    value = ''.join(first[j:i + 1])
                    first_dict[key] = value
                    j = i + 1
                    key += 1
            if inp_index in first_dict.keys():
                first_dict[inp_index] = ""
                clear_file("first.csv")
                with open("first.csv", 'a', encoding="utf-8") as f:
                    for key in first_dict.keys():
                        f.write(first_dict[key])
            else:
                delete_data()

    elif inp == 2:
        inp_index = int(input("Введите номер записи для удаления -> "))
        with open("second.csv", 'r', encoding="utf-8") as f:
            second = f.readlines()
            second_dict = {}
            key = 1
            for i in range(len(second)):
                if second[i] != '\n':
                    second_dict[key] = second[i] + '\n'
                    key += 1
            if inp_index in second_dict.keys():
                second_dict[inp_index] = ""
                clear_file("second.csv")
                with open("second.csv", 'a', encoding="utf-8") as f:
                    for key in second_dict.keys():
                        f.write(second_dict[key])
            else:
                delete_data()

