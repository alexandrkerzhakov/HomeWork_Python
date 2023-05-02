# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def get_list(size):
    new_list = []
    for i in range(size):
        new_list.append(get_random_number())
    return new_list


def get_dict_index_from_range(min, max, list):
    new_list = []
    for value in list:
        if min < value < max:
            index = random_list.index(value)
            if value not in new_list:
                new_list.append(index)
                list[index] = 0
    return new_list


if __name__ == '__main__':
    size = int(input("Вводим размер списка -> "))
    random_list = get_list(size)
    print(f"Выводим список -> {random_list}")
    min = input(f"Вводим минимум диапазона -> ")
    max = input(f"Вводим максимум диапазона -> ")
    lindex_from_range_list = get_dict_index_from_range(int(min), int(max), random_list)
    print(f"Выводим список с индексами элементов (min < value < max) -> {lindex_from_range_list}")
