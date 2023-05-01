# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
import numpy


def get_coin_array(n):
    coin_array = numpy.zeros(int(n)).astype(int)
    for i in range(coin_array.size):
        coin_array[i] = random.randint(0, 1)
    return coin_array


def get_print_array_of_coin(coin_arr):
    print("Выводим элементы массива в консоль -> ", end="")
    for value in coin_arr:
        print(value, end=" ")


def get_count_flipped_coin(coin_arr):
    count_tail_of_coin = 0 # монеты решкой вверх
    count_coat_of_coin = 0 # монеты гербом вверх
    for value in coin_arr:
        if value == 0:
            count_tail_of_coin += 1
        else:
            count_coat_of_coin += 1
    if count_coat_of_coin >= count_tail_of_coin:
        return count_tail_of_coin
    else:
        return count_coat_of_coin


if __name__ == '__main__':
    coin_array = get_coin_array(int(input("Введите количество монет -> ")))
    get_print_array_of_coin(coin_array)
    coin = get_count_flipped_coin(coin_array)
    print(f"\nНеобходимо перевернуть следующее количество монет -> {coin}")
