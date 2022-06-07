"""
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

file_1 = open('Alex_Pikul_Lesson_6_ex_1/nginx_logs.txt', 'r', encoding='utf-8')


def fnd_spammer(any_log_file):
    ip_lst = []

    for ip in any_log_file:
        ip_lst.append(any_log_file.readline().split(' ')[0])

    unic_ip = set(ip_lst)

    spammer = {}
    for ip in unic_ip:
        a = ip_lst.count(ip)
        spammer[ip] = a

    return spammer


print(fnd_spammer(file_1))








