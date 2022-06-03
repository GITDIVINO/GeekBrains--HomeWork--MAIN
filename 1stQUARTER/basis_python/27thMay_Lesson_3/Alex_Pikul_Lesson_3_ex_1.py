"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""


# Думаю лучше хранить информацию внутри функции, так как её можно будет использовать в любом файле, импортируя функцию
# из модуля
def num_translate(any_num):
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

    return internal_dict[any_num]


# список со значениями, которые нужно получить от пользователя
eng_num_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
what_number = None

# Запрос числа от пользователя и вызов функции
while what_number not in eng_num_lst:
    what_number = input('Введите число на англйском от 0 до 10, которое нужно перевести: ')
else:
    print(f'"{what_number}" перевод на русский - {num_translate(what_number)}')


print('_' * 50)


# перебор элементов в спике и передача их в функцию
for what_number in eng_num_lst:
    print(f'"{what_number}" перевод на русский - {num_translate(what_number)}')




