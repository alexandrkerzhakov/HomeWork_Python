# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
import array

import numpy


def get_array(number):
    array = numpy.zeros(6).astype(int)
    for i in range(6):
        array[i] = number % 10
        number = number // 10
    return array


def is_happy_ticket(array):
    sumLeft = 0
    sumRight = 0
    for i in range(len(array)):
        if i < len(array) // 2:
            sumLeft += array[i]
        else:
            sumRight += array[i]
    if sumLeft == sumRight:
        return "Yes"
    else:
        return "No"


def get_print_array(array):
    print("Выводим элементы массива в консоль -> ", end="")
    for value in array:
        print(value, end=" ")


if __name__ == '__main__':
    number = (int(input("Введите число -> ")))
    print(f"Билет: {number} счастливый? -> {is_happy_ticket(get_array(number))} ")
