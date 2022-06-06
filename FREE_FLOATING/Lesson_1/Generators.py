"""Practice with generators"""

import random
from itertools import islice
from sys import getsizeof

num_gen = (random.randint(1, 300) for i in range(5))
# print(next(num_gen))
# print(next(num_gen))

print(*islice(num_gen, 10))

num_gen_2 = (random.randint(1, 300) for i in range(5))
print(type(num_gen_2), *num_gen_2, id(num_gen_2), getsizeof(num_gen_2))
