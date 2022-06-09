"""
5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
файлов и имя выходного файла. Проверить работу скрипта
"""

initial_file_1 = input('Введите имя 1-го исходного файла: ')
initial_file_2 = input('Введите имя 2-го исходного файла: ')
result_file = input('Введите имя финального файла: ')

#   помещаем всё внутрь создаваемого файла 'users_hobby.txt'
with open(f'{result_file}.txt', 'w', encoding='utf-8') as data:

    with open(f'{initial_file_1}.csv', 'r', encoding='utf-8') as users:
        name_lst = [name[:-1].replace(',', ' ') for name in users]

    with open(f'{initial_file_2}.csv', 'r', encoding='utf-8') as hobbys:
        hobby_lst = hobbys.readline().replace(' ', '').split(',')

    #   прописываем условие записи в файл, без создания словаря
    i = 0
    while i < len(name_lst) and i < len(hobby_lst):
        data.write(f'{name_lst[i]}: {hobby_lst[i]}')
        i += 1
    while i < len(name_lst) > len(hobby_lst) :
        data.write(f'{name_lst[i]}: {None}')
        i += 1








