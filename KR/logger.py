from other_functions import clear_file
from data_create import get_id, get_title, get_body, get_date


def input_data():
    id = get_id()
    title = get_title()
    body = get_body()
    date = get_date()
    inp = input(f"\n Записать данные (формат -> строка):"
                f"\n{id}; {title}; {body}; {date}"
                "\nВыберите вариант -> (yes)")
    while inp != "yes":
        print("Некорректно введены данные")
        inp = input("Записать данные (формат -> строка):"
                    "\nВыберите вариант -> (yes)")
    if inp == "yes":
        with open("note.csv", 'a', encoding="utf-8") as f:
            f.write(f"{id}; {title}; {body}; {date}\n\n")


def print_data():
    print("Вывожу данные из файла c заметками: \n")
    with open("note.csv", 'r', encoding="utf-8") as f:
        second = f.readlines()
        print(second)


def update_data():
    inp_index = int(input("Введите номер записи для редактирования -> "))
    with open("note.csv", 'r', encoding="utf-8") as f:
        second = f.readlines()
        second_dict = {}
        key = 1
        for i in range(len(second)):
            if second[i] != '\n':
                second_dict[key] = second[i] + '\n'
                key += 1
        if inp_index in second_dict.keys():
            id = get_id()
            title = get_title()
            body = get_body()
            date = get_date()
            second_dict[inp_index] = f"{id}; {title}; {body}; {date}\n\n"
            clear_file("note.csv")
            with open("note.csv", 'a', encoding="utf-8") as f:
                for key in second_dict.keys():
                    f.write(second_dict[key])
        else:
            update_data()


def delete_data():
    inp_index = int(input("Введите номер записи для удаления -> "))
    with open("note.csv", 'r', encoding="utf-8") as f:
        second = f.readlines()
        second_dict = {}
        key = 1
        for i in range(len(second)):
            if second[i] != '\n':
                second_dict[key] = second[i] + '\n'
                key += 1
        if inp_index in second_dict.keys():
            second_dict[inp_index] = ""
            clear_file("note.csv")
            with open("note.csv", 'a', encoding="utf-8") as f:
                for key in second_dict.keys():
                    f.write(second_dict[key])
        else:
            delete_data()
