"""Use map() instead of for"""

import random

numbers = [random.randint(1, 20) for i in range(10)]
print(f'{len(numbers)} values in list: {numbers}')

sqre_numbers = [number ** 2 for number in numbers]
print(f'Square of values: {sqre_numbers}')

# use map()
m_sqre_numbers = list(map(lambda number: number ** 2, numbers))
print(f'Square of values by map(lambda): {m_sqre_numbers}')
