"""
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

file_1 = open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\1stQUARTER\basis_python\07thJune_Lesson_6'
              r'\Alex_Pikul_Lesson_6_ex_1\nginx_logs.txt', 'r', encoding='utf-8')


def fnd_spammer(any_log_file):
    """Функция принимает файл с логами сайта"""
    with open('ip_list.txt', 'w+', encoding='utf-8') as f:  # отделяем ip адреса и записываем в файл ip_list.txt
        for line in any_log_file:
            f.writelines(f'{line.split(" ")[0]}\n')

    # открываем файл ip_list.txt
    file_unc_ip = open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\1stQUARTER\basis_python'
                       r'\07thJune_Lesson_6\Alex_Pikul_Lesson_6_ex_2\ip_list.txt', 'r', encoding='utf-8')

    ip_lst = [line.strip() for line in file_unc_ip]     # заносим ip адреса в список

    # проходим по списку и ловим спамера
    max_quan = 1
    spammer_ip = None
    for ip in ip_lst:
        req_quan = ip_lst.count(ip)
        if req_quan > max_quan:
            max_quan = req_quan
            spammer_ip = ip

    return spammer_ip, max_quan


print(f'Спамер: {fnd_spammer(file_1)} запросов')
