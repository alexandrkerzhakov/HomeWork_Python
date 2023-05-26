# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def get_personal_count(sum):
    for i in range(sum):
        if i + i * 2 * 2 + i == sum:
            return f"Petr -> {i}, Katya -> {i * 2 * 2}, Sergey -> {i}"
    return "Invalid date"

if __name__ == '__main__':
    sum = (int(input("Введите число сделанных журавликов -> ")))
    print(f"Личные показатели -> {get_personal_count(sum)}")
