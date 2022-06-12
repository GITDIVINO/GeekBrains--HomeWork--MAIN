"""
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт
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
    with open(f'{any_directory}_summary.json', 'w', encoding='utf-8') as f:
        f.write(str(stat_of_folder))

    return stat_of_folder


if __name__ == '__main__':
    directory = input('Please enter directory: ')
    print(make_stat(directory))

