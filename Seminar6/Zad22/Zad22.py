# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def get_list(size):
    new_list = []
    for i in range(int(size)):
        new_list.append(get_random_number())
    return new_list


def get_unique_sort_list_from_two_list(list1, list2):
    unique_list = list(set(list1) & set(list2))
    unique_list.sort()
    return unique_list


if __name__ == '__main__':
    size_of_list1 = input("Вводим размер списка №1 -> ")
    size_of_list2 = input("Вводим размер списка №2 -> ")
    list1 = get_list(size_of_list1)
    print(f"Выводим список 1 -> {list1}")
    list2 = get_list(size_of_list2)
    print(f"Выводим список 2 -> {list2}")
    unique = get_unique_sort_list_from_two_list(list1, list2)
    print(f"Выводим отсортированный список (пересечение списка №1 и списка №2) -> {unique}")

