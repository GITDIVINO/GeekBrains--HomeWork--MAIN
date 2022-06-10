"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
"""

import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = str(requests.get(URL).text)

# Запишем логи сайта в файл 'nginx_logs.txt'
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(response)

file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')


def get_info(any_file):
    result = []

    for i in any_file:
        line = any_file.readline().split(' ')
        result.append((line[0], line[5].replace('"', ''), line[6]))

    any_file.close()

    return result


# запишем результат в файл
with open('parsed_nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(str(get_info(file_1)))
