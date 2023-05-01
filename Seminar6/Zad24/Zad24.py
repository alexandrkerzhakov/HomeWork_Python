# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def get_dict_bushes_berries(count):
    bb_dict = {i: get_random_number() for i in range(1, int(count) + 1)}
    return bb_dict


def get_dict_bushes_berries_from_2neighbors(bb_dict):
    bb_fr_2neighbors_dict = {}
    for i in range(1, len(bb_dict) + 1):
        bushes = bb_dict.get(i)
        bushes_right = bb_dict.get(i + 1)
        bushes_left = bb_dict.get(i - 1)
        if i == 1:
            bushes_left = bb_dict.get(len(bb_dict))
        elif i == int(count_bushes):
            bushes_right = bb_dict.get(1)
        bb_fr_2neighbors_dict[i] = bushes_left + bushes + bushes_right
    return bb_fr_2neighbors_dict


def get_sort_dict_bushes_berries_from_2neighbors(bb_fr_2neighbors):
    sorted_bb_fr_2n_dict = dict(sorted(bb_fr_2neighbors.items(), key=lambda item: item[1]))
    return sorted_bb_fr_2n_dict


def get_search_bushes(sorted_bb_fr_2n_dict):
    temp_list = list(sorted_bb_fr_2n_dict.keys())
    return temp_list[-1]


if __name__ == '__main__':
    count_bushes = input("Вводим количество кустов на грядке -> ")
    bb_dict = get_dict_bushes_berries(count_bushes)
    print(f"Выводим словарь => куст : ягоды -> {bb_dict}")
    bb_fr_2neighbors_dict = get_dict_bushes_berries_from_2neighbors(bb_dict)
    print(f"Выводим словарь => куст : сумма ягод с куста и двух соседних -> {bb_fr_2neighbors_dict}")
    sorted_bb_fr_2n_dict = get_sort_dict_bushes_berries_from_2neighbors(bb_fr_2neighbors_dict)
    print(f"Выводим отсортированный по значению словарь => куст : сумма ягод с куста и двух соседних -> {sorted_bb_fr_2n_dict}")
    search_bushes = get_search_bushes(sorted_bb_fr_2n_dict)
    print(f"Оптимальный куст для сбора ягод -> {search_bushes}")

