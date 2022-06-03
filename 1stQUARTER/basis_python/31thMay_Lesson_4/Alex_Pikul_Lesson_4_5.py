"""
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
python task_4_5.py USD
75.18, 2020-09-05
"""

import sys
sys.path.append('C:/Users/User/Desktop/GeekBrains/GeekBrains__HomeWork__MAIN/1stQUARTER/basis_python/31thMay_Lesson_4')
from Alex_Pikul_Lesson_4_2 import *


def main(argv):
    program, *args = argv
    currency_rates(argv)
    result = sum(map(int, args))
    print(f'результат: {result}')

    return result

input()

if __name__ == '__main__':
    import sys

    exit(main(sys.argv))















