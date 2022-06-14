"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
--- email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
--- email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

#   перед прочтением методички :)
# def email_parse(any_email_address):
#     result_dict = {}
#     try:
#         if re.search('@', any_email_address) and re.search('\.ru', any_email_address):
#             result = re.split(r'@', any_email_address)
#             result_dict['username'] = result[0]
#             result_dict['domain'] = result[1]
#         else:
#             raise ValueError
#
#     except ValueError:
#         return print(f'wrong email: {any_email_address}')
#
#     return result_dict

#   после прочтения методички
VALID_EMAIL = re.compile(r'^\w*@\w*\.(com|ru|bk)$')


def email_parse_2(any_email_address):
    result_dict = {}

    try:
        if VALID_EMAIL.match(any_email_address):
            result = re.split(r'@', any_email_address)
            result_dict['username'] = result[0]
            result_dict['domain'] = result[1]
        else:
            raise ValueError

    except ValueError:
        return print(f'ValueError: wrong email: {any_email_address}')

    return result_dict


if __name__ == '__main__':
    # print(email_parse(input('Please enter email: ')))
    print(email_parse_2(input('Please enter email: ')))


