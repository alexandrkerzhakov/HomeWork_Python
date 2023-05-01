import random
import numpy


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

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


def get_count_of_duplicate(number, array):
    count_of_duplicate = 0
    for value in array:
        if (value == number):
            count_of_duplicate += 1
    return count_of_duplicate


if __name__ == '__main__':
    number_array = get_array(int(input("Введите длину массива (N) -> ")))
    get_print_array(number_array)
    X = get_random_number()
    print(f"\nЧисло для поиска -> {X}")
    print(f"Количество повторений числа {X} в массиве -> {get_count_of_duplicate(X, number_array)}")
