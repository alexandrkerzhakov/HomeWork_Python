from other_functions import clear_file
from data_create import get_id, get_title, get_body, get_date


def input_data():
    id = get_id()
    title = get_title()
    body = get_body()
    date = get_date()
    inp = input(f"\n Записать данные (формат -> строка):"
                f"\n{id}; {title}; {body}; {date}"
                "\nВыберите вариант (y/n) -> ")
    while inp != "y":
        print("Некорректно введены данные")
        inp = input("Записать данные (формат -> строка):"
                    "\nВыберите вариант (y/n) -> ")
    if inp == "y":
        with open("note.csv", 'a', encoding="utf-8") as f:
            f.write(f"{id}; {title}; {body}; {date}\n\n")


def print_data():
    inp = int(input("Выбери вариант для вывода данных в консоль (1/2): "
                    "\n1 -> Вывод записи по дате"
                    "\n2 -> Вывод записи по идентификатору"
                    "\n3 -> Выбор всего списка заметок"
                    "\nВыбор -> "))
    if inp == 1:
        # date = int(input("Введите дату для вывода заметки в консоль -> "))
        # with open("note.csv", 'r', encoding="utf-8") as f:
        #     note = f.readlines()
        #     note_dict = {}
        #     key = 1
        #     for i in range(len(note)):
        #         if note[i] != '\n':
        #             note_dict[key] = note[i] + '\n'
        #             key += 1
        #     list_with_date = []
        #     [list_with_date.append(note) for note in dict.keys() if date in dict.keys()]
        #     print(note_dict[inp_index])

        date = input("Введите дату для вывода заметки в консоль -> ")
        with open("note.csv", 'r', encoding="utf-8") as f:
            note_list = f.readlines()
            for note in note_list:
                if note.__contains__(date):
                    print(note)
    elif inp == 2:
        inp_index = int(input("Введите номер записи для вывода в консоль -> "))
        with open("note.csv", 'r', encoding="utf-8") as f:
            note_list = f.readlines()
            note_dict = {}
            key = 1
            for i in range(len(note_list)):
                if note_list[i] != '\n':
                    note_dict[key] = note_list[i] + '\n'
                    key += 1
            print(note_dict[inp_index])

    elif inp == 3:
        print("Вывожу данные из файла c заметками: \n")
        with open("note.csv", 'r', encoding="utf-8") as f:
            note = f.readlines()
            print(note)

    else:
        print_data()


def update_data():
    inp_index = int(input("Введите номер записи для редактирования -> "))
    with open("note.csv", 'r', encoding="utf-8") as f:
        note = f.readlines()
        note_dict = {}
        key = 1
        for i in range(len(note)):
            if note[i] != '\n':
                note_dict[key] = note[i] + '\n'
                key += 1
        if inp_index in note_dict.keys():
            id = get_id()
            title = get_title()
            body = get_body()
            date = get_date()
            note_dict[inp_index] = f"{id}; {title}; {body}; {date}\n\n"
            clear_file("note.csv")
            with open("note.csv", 'a', encoding="utf-8") as f:
                for key in note_dict.keys():
                    f.write(note_dict[key])
        else:
            update_data()


def delete_data():
    inp_index = int(input("Введите номер записи для удаления -> "))
    with open("note.csv", 'r', encoding="utf-8") as f:
        note = f.readlines()
        note_dict = {}
        key = 1
        for i in range(len(note)):
            if note[i] != '\n':
                note_dict[key] = note[i] + '\n'
                key += 1
        if inp_index in note_dict.keys():
            note_dict[inp_index] = ""
            clear_file("note.csv")
            with open("note.csv", 'a', encoding="utf-8") as f:
                for key in note_dict.keys():
                    f.write(note_dict[key])
        else:
            delete_data()
