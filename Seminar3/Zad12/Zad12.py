import random


# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


def get_random_number():
    number = random.randint(1, 100)
    return number


def selection_pair_of_values(sum, multiplication):
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i + j == sum and i * j == multiplication:
                return f"Загаданные числа -> {i}, {j}"


if __name__ == '__main__':
    X = get_random_number()
    Y = get_random_number()
    sum_of_values = X + Y
    multiplication_of_values = X * Y
    print(f"Сумма чисел равна -> {sum_of_values}")
    print(f"Произведение чисел равно -> {multiplication_of_values}")
    print(selection_pair_of_values(sum_of_values, multiplication_of_values))
