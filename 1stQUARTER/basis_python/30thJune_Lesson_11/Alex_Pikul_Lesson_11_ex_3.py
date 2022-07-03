"""
3. Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться
"""


class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text


def make_only_digit_lst(user_d=0):
    """With helps of this func we`ll check is 'user_d' digit or not, if positive it`ll be added to 'user_d_lst',
    if not, we`ll handle it with NotNumberError exception"""

    user_d_lst = []
    while user_d != 'stop':
        try:
            user_d = input('Please enter digit to add at the list: ')
            if not user_d.isdigit():
                raise NotNumberError(f'-<|>- ERROR: NotNumberError: "{user_d}" is not a digit -<|>-')
            user_d_lst.append(user_d)
            print(f'"{user_d}" is a digit, added to the user_d_lst')
        except NotNumberError as err:
            print(err)

    print(f'<---- List with digits: {user_d_lst} ---->')


if __name__ == '__main__':
    make_only_digit_lst()










