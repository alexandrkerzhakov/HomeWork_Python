import random
import numpy


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

def get_random_number():
    number = random.randint(1, 100)
    return number


def get_array(N):
    coin_array = numpy.zeros(int(N)).astype(int)
    for i in range(coin_array.size):
        coin_array[i] = get_random_number()
    return coin_array


def get_print_array(array):
    print("Выводим элементы массива в консоль -> ", end="")
    for value in array:
        print(value, end=" ")


def get_min_diff_number(number, array):
    min_diff = number
    min_diff_number = array[0]
    for value in array:
        diff = abs(number - value)
        if diff < min_diff:
            min_diff = diff
            min_diff_number = value
    return min_diff_number


if __name__ == '__main__':
    number_array = get_array(int(input("Введите длину массива (N) -> ")))
    get_print_array(number_array)
    X = get_random_number()
    print(f"\nЧисло для поиска самого близкого к нему по величине -> {X}")
    print(f"Самое близкое к числу {X} в массиве -> {get_min_diff_number(X, number_array)}")
