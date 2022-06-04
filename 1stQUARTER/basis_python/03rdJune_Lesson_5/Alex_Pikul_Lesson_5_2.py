"""
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def num_gen(start, end):
    gen_numbers = (num for num in range(start, end + 1, 2))
    return gen_numbers


print(*num_gen(1, 15))









