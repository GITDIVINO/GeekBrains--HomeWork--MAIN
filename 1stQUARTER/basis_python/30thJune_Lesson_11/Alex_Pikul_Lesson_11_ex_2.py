"""
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, вводимых
пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class Myown_ZeroDivisionError(Exception):
    """Exception prevent attempts destroy the math -> universe"""
    def __init__(self, text):
        self.text = text


def divide_nums(first_num=0, second_num=0):
    while True:
        print('|-----Let`s divide two numbers!-----|')
        first_num = int(input('Please enter first number: '))
        second_num = int(input('Please enter second number: '))
        if second_num == 0:
            raise Myown_ZeroDivisionError('ERROR: It`s danger to divide by zero. Try again :)')
        else:
            print(f'Result: {first_num/second_num}  <|>---Division is successful---<|>')


if __name__ == '__main__':

    try:
        divide_nums()
    except Myown_ZeroDivisionError as err:
        print(err)

    print('\n[---> Some code to prove exception is working <---]')