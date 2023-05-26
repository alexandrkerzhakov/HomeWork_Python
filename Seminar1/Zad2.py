# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def get_sum_of_number(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


if __name__ == '__main__':
    number = (int(input("Введите число -> ")))
    print(f"Сумма цифр числа -> {get_sum_of_number(number)}")
