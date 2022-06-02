"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
"""

import requests
import json
import datetime as dt
URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = requests.get(URL)

data = response.text.split('</Valute>')   # разделяем данные полученные по запросу

# сортируем информацию
money_code_lst = [i[(i.find('<CharCode>') + len('<CharCode>')): i.find('</CharCode>')] for i in data]   # по коду
nominal_lst = [i[(i.find('<Nominal>') + len('<Nominal>')): i.find('</Nominal>')] for i in data]     # по номиналу
money_name_lst = [i[(i.find('<Name>') + len('<Name>')): i.find('</Name>')] for i in data]   # по названию
value_lst = [i[(i.find('<Value>') + len('<Value>')): i.find('</Value>')].replace(',', '.') for i in data]   # по курсу
date = response.headers['Date']     # вытягиваем дату из хедера в формате str


def currency_rates(any_money_name):
    """функция принимает буквенный код валюты и возвращает курс и полное названиие на русском"""
    try:
        index = money_code_lst.index(any_money_name)
    except ValueError:
        return None
    return f'На {date} {money_name_lst[index]} равен {float(value_lst[index])/float(nominal_lst[index])} рублей'


# Принимаем код валюты от пользователя
chse = ((input(f'Список валют:\n{money_code_lst}\nЧто бы получить курс, введите код валюты из списка выше: ')).upper())
print(currency_rates(chse))














