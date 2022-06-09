"""Скрипт читающий файл"""

import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:  #  условие — выводить все записи
        print(f.read())
    if len(sys.argv) == 2:  #  условие — ввыводить все записи с номера, равного этому числу, до конца
        for line in f.readlines()[int(sys.argv[1]) - 1:]:
            print(line.strip())
    if len(sys.argv) == 3:  #  условие —  начиная с номера, равного первому числу, по номер, равный второму числу
        for line in f.readlines()[int(sys.argv[1]) - 1:int(sys.argv[2]) + 1]:
            print(line.strip())




