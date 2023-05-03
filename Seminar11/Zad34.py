# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def get_dict_word_count_vowel(list):
    dict_word_count_vowel = {}
    for word in list:
        count_vowel = 0
        for char in word:
            if char in list_vowel:
                count_vowel += 1
        dict_word_count_vowel[word] = count_vowel
    return dict_word_count_vowel


def get_rhythm(dict):
    begin_count = list(dict.values())[0]
    for count_vowel in dict.values():
        if count_vowel != begin_count:
            return "Пам парам"
    return "Парам пам-пам"


if __name__ == '__main__':
    list_vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    line = input("Вводим кричалку -> ")
    word_list = list(line.split(" "))
    print(f"Выводим список слов -> {word_list}")
    dict_word_count_vowel = get_dict_word_count_vowel(word_list)
    print(f"Выводим словарь слов с количеством гласных букв -> {dict_word_count_vowel}")
    print(f"Итоговая фраза - Парам пам-пам/Пам парам -> {get_rhythm(dict_word_count_vowel)}")
