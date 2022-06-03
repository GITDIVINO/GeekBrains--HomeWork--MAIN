"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
- next(odd_to_15)
1
- next(odd_to_15)
3
...
- next(odd_to_15)
15
- next(odd_to_15)
...StopIteration...
"""


def odd_to_n(start, end):
    for num in range(start, end + 1):
        yield num


print(*(odd_to_n(1, 15)), sep='\n')















