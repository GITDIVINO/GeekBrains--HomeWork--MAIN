"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""

import requests

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = requests.get(URL)

data = response.text.split('</Valute>')   # разделяем данные полученные по запросу

# сортируем информацию
money_code_lst = [i[(i.find('<CharCode>') + len('<CharCode>')): i.find('</CharCode>')] for i in data]   # по коду
nominal_lst = [i[(i.find('<Nominal>') + len('<Nominal>')): i.find('</Nominal>')] for i in data]     # по номиналу
money_name_lst = [i[(i.find('<Name>') + len('<Name>')): i.find('</Name>')] for i in data]   # по названию
value_lst = [i[(i.find('<Value>') + len('<Value>')): i.find('</Value>')].replace(',', '.') for i in data]   # по курсу


def currency_rates(any_money_name):
    """функция принимает буквенный код валюты и возвращает курс и полное названиие на русском"""
    try:
        index = money_code_lst.index(any_money_name)
    except ValueError:
        return None
    return f'{money_name_lst[index]} равен {float(value_lst[index])/float(nominal_lst[index])} рублей'


# Принимаем код валюты от пользователя
chse = ((input(f'Список валют:\n{money_code_lst}\nЧто бы получить курс, введите код валюты из списка выше: ')).upper())
print(currency_rates(chse))
