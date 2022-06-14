"""
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET/downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

import re
import requests

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = str(requests.get(URL).text)

# paresed_ip = re.search(r'\d*\.\d*\.\d*\.\d*', response)
# print(paresed_ip)
# paresed_date = re.search(r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}', response)
# print(paresed_date)
# paresed_request_type = re.search(r'(POST|GET|PUT|OPTION|HEAD)', response)
# print(paresed_request_type)
# paresed_requested_resource = re.search(r'(/\w{9}/\w{9})', response)
# print(paresed_requested_resource)
# paresed_response_code_and_size = re.search(r'\d{3}\s\d+', response)
# print(paresed_response_code_and_size)

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(response)

# file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
# print(file_1.readline(), type(file_1.readline()))

with open('parsed_nginx_logs.txt', 'w', encoding='utf-8') as f:
    file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')

    for line in file_1:
        try:
            data = [re.search(r'\d*\.\d*\.\d*\.\d*', line).group(0),
                    re.search(r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}', line).group(0),
                    re.search(r'(POST|GET|PUT|OPTION|HEAD)', line).group(0),
                    re.search(r'(/\w{9}/\w{9})', line).group(0),
                    re.search(r'\d{3}\s\d+', line).group(0).split(' ')[0],
                    re.search(r'\d{3}\s\d+', line).group(0).split(' ')[1]]
            f.writelines(str(data) + '\n')
        except AttributeError:
            continue

# data = [re.search(r'(\d*\.\d*\.\d*\.\d*)(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})(POST|GET|PUT|OPTION|HEAD)(/\w{9}/\w{9})(\d{3}\s\d+)', response).group(0)]
