"""3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться."""

# список, котрый нужно обработать
some_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

""" Должны получить на выходе строку: в "05" часов "17" минут температура воздуха была "+05" градусов"""

for element in some_lst:
    if element.startswith('+'):
        _index = some_lst.index(element)
        if int(element[1:]) // 10 == 0:
            some_lst[_index] = f'"+0{element[1:]}"'

    if element.isdigit():
        _index = some_lst.index(element)
        if int(element) // 10 == 0:
            element = '0' + element
        some_lst[_index] = f'"{element}"'


print(' '.join(some_lst))





