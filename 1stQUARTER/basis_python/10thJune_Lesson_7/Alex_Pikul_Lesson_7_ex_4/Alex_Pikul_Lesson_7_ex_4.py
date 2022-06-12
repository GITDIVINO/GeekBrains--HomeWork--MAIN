"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
from pathlib import Path as P


def make_stat(any_directory):
    stat_of_folder = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0
    }
    any_pth = P.cwd()

    for file in os.listdir(fr'{any_pth}\{any_directory}'):
        if os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 100:
            stat_of_folder[100] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 1000:
            stat_of_folder[1000] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 10000:
            stat_of_folder[10000] += 1
        else:
            stat_of_folder[100000] += 1

        # print(os.stat(fr'{any_pth}\{any_directory}\{file}').st_size)

    return stat_of_folder


if __name__ == '__main__':
    directory = input('Please enter directory: ')
    print(make_stat(directory))



