"""
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, вводимых
пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class Myown_ZeroDivisionError(Exception):
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num


if __name__ == '__main__':
    first_num = int(input('Please enter first number: '))
    second_num = int(input('Please enter second number: '))

    try:
        print(first_num / second_num)
        if second_num == 0:
            raise Myown_ZeroDivisionError('Myown_ZeroDivisionError: division by zero')
    except Myown_ZeroDivisionError as err:
        print(err)
    else:
        print(f'All is ok. {first_num} / {second_num} = {first_num/second_num}')