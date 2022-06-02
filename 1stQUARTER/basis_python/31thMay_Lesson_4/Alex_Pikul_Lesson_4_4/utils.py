import sys

sys.path.append('C:/Users/User/Desktop/GeekBrains/GeekBrains__HomeWork__MAIN/1stQUARTER/basis_python/31thMay_Lesson_4')
from Alex_Pikul_Lesson_4_2 import *


chse = ((input(f'Список валют:\n{money_code_lst}\nЧто бы получить курс, введите код валюты из списка выше: ')).upper())
print(currency_rates(chse))
