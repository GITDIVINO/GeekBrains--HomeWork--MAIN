"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с
сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def make_unc_lst(any_list):
    """The function take any list and give list with unic elemints"""
    result = []

    for element in any_list:
        if any_list.count(element) == 1:
            result.append(element)

    return result


print(make_unc_lst(src))


def upt_make_unc_lst(any_list):
    """Updated function"""
    result = [element for element in any_list if any_list.count(element) == 1]

    return result


print(upt_make_unc_lst(src))
