# *Задача 20: * В настольной игре Скрабл (Scrabblist_letters_pointse) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, list_letters_points, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12
import sys


def scrab_of_leter_from_dict(letter, dict):
    if dict.get(letter):
        return dict.get(letter)
    else:
        return 0


def get_scrab_word(input_word, input_language):
    scrab_word = 0
    if input_language == "ru":
        for letter in input_word:
            scrab_of_letter = scrab_of_leter_from_dict(letter.upper(), dict_ru)
            scrab_word += scrab_of_letter
    elif input_language == "en":
        for letter in input_word:
            scrab_of_letter = scrab_of_leter_from_dict(letter.upper(), dict_en)
            scrab_word += scrab_of_letter
    else:
        print(f"Язык текста \"{input_language}\" введен ошибочно, необходимо выбирать из (ru/en)")
        sys.exit()
    return scrab_word


if __name__ == '__main__':
    dict_ru = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2,
               'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5,
               'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

    dict_en = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3,
               'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

    word = input("Вводим слово -> ")
    language = input("Вводим язык написания текста(слова) (ru/en) -> ")
    print(f"Ценность слова \"{word}\" -> {get_scrab_word(word, language)}")
