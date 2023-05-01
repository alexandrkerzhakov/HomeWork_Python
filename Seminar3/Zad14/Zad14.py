import random


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def get_random_number():
    number = random.randint(1, 100)
    return number


def get_powers_of_two(N):
    for i in range(N):
        pow = 2 ** i
        if pow <= N:
            print(pow, end=" ")


if __name__ == '__main__':
    N = get_random_number()
    print(f"Число N: -> {N}")
    print("Последовательность чисел (степеней двойки) <= N -> ", end="")
    get_powers_of_two(N)
