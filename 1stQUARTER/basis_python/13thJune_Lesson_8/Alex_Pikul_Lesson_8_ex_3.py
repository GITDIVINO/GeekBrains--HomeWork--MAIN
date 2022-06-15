"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
--- a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
--- a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    def wrapper(*args):
        result = {i: type(i) for i in args}
        return result
    return wrapper


@type_logger
def calc_cube(*args):
    res = [arg**3 for arg in args]
    return res


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    b = calc_cube(12, 8)
    print(b)
