import os
import sys


def start_project():
    dir_name = ['settings', 'mainapp', 'adminapp', 'authapp', 'my_project']

    if not os.path.exists(str(sys.argv[1])):
        os.mkdir(str(sys.argv[1]))
        os.chdir(str(sys.argv[1]))

    for d in dir_name:
        if not os.path.exists(d):
            os.mkdir(d)

    return print('Стартер создал структуру проекта')


start_project()
