"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random


# напишем ф-ю возвращающую рандомное слово из списка
def rnd_word(any_word_lst):
    word = any_word_lst[random.randint(0, len(any_word_lst) - 1)]
    return word


def get_jokes(jokes_quantity):
    """Функция принимает количество шуток и возвращет n шутков, сформированных из трех случайных слов"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    return [f'{rnd_word(nouns)} {rnd_word(adverbs)} {rnd_word(adjectives)}' for i in range(jokes_quantity)]


# запрашиваем желаемое количество шуток у пользователя и вызываем функцию
how_many = int(input('Введите количество шуток: '))
print(get_jokes(how_many))