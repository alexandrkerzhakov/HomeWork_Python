# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def sum(A, B):
    if B == 0:
        return A
    return 1 + sum(A, B - 1)


if __name__ == '__main__':
    A = get_random_number()
    B = get_random_number()
    print(f"Сумма числа {A} и числа {B} -> {sum(A, B)}")
