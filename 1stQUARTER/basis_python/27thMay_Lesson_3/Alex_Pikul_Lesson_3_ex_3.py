"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    name_dict = {}

    for name in args:
        name_dict[name[0]] = name_dict.get(name[0], []) + [name]

    return name_dict


# вызываем ф-ю
print(thesaurus('Алексей', 'Андрей', 'Борис', 'Елена', 'Егор'))


"""Решение через библиотеку collections"""

# from collections import defaultdict
#
#
# def thesaurus(any_name_lst):
#     name_dict = defaultdict(list)
#
#     for name in any_name_lst:
#         name_dict[name[0]].append(name)
#
#     return name_dict
#
#
# # Запросим имена у пользователя и внесём в список
# name_lst = [input(f'Введите имя (осталось {5 - i}): ') for i in range(5)]
#
# print(thesaurus(name_lst))
