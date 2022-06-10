"""
4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь с
данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и
пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""

import itertools

#   помещаем всё внутрь создаваемого файла 'users_hobby.txt'
with open('users_hobby.txt', 'w', encoding='utf-8') as data:

    with open('users.csv', 'r', encoding='utf-8') as users:
        name_lst = [name[:-1].replace(',', ' ') for name in users]

    with open('hobby.csv', 'r', encoding='utf-8') as hobbys:
        hobby_lst = hobbys.readline().replace(' ', '').split(',')

    #   прописываем условие записи в файл, без создания словаря
    i = 0
    while i < len(name_lst) and i < len(hobby_lst):
        data.write(f'{name_lst[i]}: {hobby_lst[i]}')
        i += 1
    while i < len(name_lst) > len(hobby_lst) :
        data.write(f'{name_lst[i]}: {None}')
        i += 1








