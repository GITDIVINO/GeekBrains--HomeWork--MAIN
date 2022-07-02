"""
7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
(комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
результата.
"""
import math


class Complex_number(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = complex(a, b)
        print(f'<-- Complex number "{self.x}" created -->')

    def __add__(self, other):
        return f'sum {self.x} and {other.x}: {complex((self.a + other.a), (self.b + other.b))}'


if __name__ == '__main__':
    first_num = Complex_number(3, 4)
    second_num = Complex_number(5, 7)
    print(first_num + second_num)






