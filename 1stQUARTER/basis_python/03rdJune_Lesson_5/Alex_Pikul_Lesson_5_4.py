"""
### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def make_new_lst(any_lst):
    amm_lst = list(zip(any_lst[1:], any_lst))
    result_lst = []

    for element in amm_lst:
        if element[1] < element[0]:
            result_lst.append(element[0])

    return result_lst


print(make_new_lst(src))
