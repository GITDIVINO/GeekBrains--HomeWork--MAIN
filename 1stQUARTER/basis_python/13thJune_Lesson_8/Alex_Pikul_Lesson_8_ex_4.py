"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
--- a = calc_cube(5)
125
--- a = calc_cube(-5)
Traceback (most recent call last):
...
raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(x):
    def _val_checker(func):
        def wrapper(*args):
            try:
                for num in args:
                    if num < 1:
                        raise ValueError
            except ValueError:
                return print(f'ValueError: wrong val {num}')
            return func(num)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    b = calc_cube(-5)
    print(b)


