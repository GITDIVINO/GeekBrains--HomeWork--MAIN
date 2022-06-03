"""
Implementation of displaying information about a period of time depending on its duration in seconds:
<d> days <h> hours <m> minutes <s> seconds
"""

import random
from main import make_better_view

# make random duration list in seconds, better to use generator to save memory
# duration_lst = (random.randint(1, 500000) for i in range(5))
# print(type(duration_lst))     # <class 'generator'>

# use for-cycle plus generator to speed up process
for duration in (random.randint(1, 500000) for i in range(5)):
    print(f'Restyle {duration} sec: {make_better_view(duration)}')
