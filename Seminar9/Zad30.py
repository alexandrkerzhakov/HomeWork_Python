# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import random


def get_random_number():
    number = random.randint(1, 10)
    return number


def get_list_arithmetic_progression(first, d, N):
    list_arithmetic_progression = []
    for i in range(1, N + 1):
        next_element = first + (i - 1) * d
        list_arithmetic_progression.append(next_element)
    return list_arithmetic_progression


if __name__ == '__main__':
    first_element = get_random_number()
    print(f"Первый элемент арифметической прогрессии -> {first_element}")
    d = get_random_number()
    print(f"Разность арифметической прогрессии -> {d}")
    N = get_random_number()
    print(f"Количество элементов арифметической прогрессии -> {N}")
    list_arithmetic_progression = get_list_arithmetic_progression(first_element, d, N)
    print(f"Арифметическая прогрессия -> {list_arithmetic_progression}")
