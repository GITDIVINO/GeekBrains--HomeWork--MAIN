"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два
"""


def num_translate_adv(any_num):
    internal_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if any_num.istitle():
        return internal_dict[any_num.lower()].capitalize()

    return internal_dict[any_num]


# список со значениями, которые нужно получить от пользователя
eng_num_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
capit_eng_num_lts = [i.capitalize() for i in eng_num_lst]
what_number = None

# Запрос числа от пользователя и вызов функции
while what_number not in eng_num_lst and what_number not in capit_eng_num_lts:
    what_number = input('Введите число на англйском от 0 до 10, которое нужно перевести: ')
else:
    print(f'"{what_number}" перевод на русский - {num_translate_adv(what_number)}')








