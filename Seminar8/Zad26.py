# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def degree(A, B):
    if B == 0:
        return 1
    return A * degree(A, B - 1)


if __name__ == '__main__':
    A = get_random_number()
    B = get_random_number()
    print(f"Число {A} в степени {B} -> {degree(A, B)}")
