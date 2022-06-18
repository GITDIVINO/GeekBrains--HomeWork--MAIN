"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    """ Класс 'Matrix' """

    matrix_count = 0

    def __init__(self, matrix_lst, matrix_lst2=None):
        Matrix.matrix_count += 1
        print(f'\n---{Matrix.matrix_count} экземпляр класса "Matrix" создан---')
        self.matrix_lst = matrix_lst
        self.matrix_lst2 = matrix_lst2

    def __str__(self):
        if self.matrix_lst2 is None:
            print('На вход поступила одна матрица:')
            for i in self.matrix_lst:
                print(" ".join(map(str, i)))
        else:
            print('Первая матрица:')
            for i in self.matrix_lst:
                print(" ".join(map(str, i)))
            print('Вторая матрица:')
            for j in self.matrix_lst2:
                print(" ".join(map(str, j)))

    def __add__(self, other):
        """Метод для вычисления суммы матриц разных объектов"""
        print('Вычисляем сумму матриц разных объектов: ')
        result = [[self.matrix_lst[i][j] + other[i][j] for j in range(len(self.matrix_lst[0]))] for i in
                  range(len(self.matrix_lst))]
        for i in result:
            print(" ".join(map(str, i)))

    def sum_matrix(self):
        """Метод для вычисления суммы матриц одного объекта"""
        if self.matrix_lst2:
            print('Вычисляем сумму 2х матриц одного объекта: ')
            result = [[self.matrix_lst[i][j] + self.matrix_lst2[i][j] for j in range(len(self.matrix_lst[0]))] for i in
                      range(len(self.matrix_lst))]
            for i in result:
                print(" ".join(map(str, i)))
        else:
            print('Сумму матриц вычислить нельзя...')


if __name__ == '__main__':
    first_matrix = Matrix([[31, 22, 56, 89], [37, 43, 76, 8]])
    first_matrix.__str__()

    second_matrix = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])
    second_matrix.__str__()

    first_matrix.__add__(second_matrix.matrix_lst)  # складываем матрицы 2х объектов

    two_matrix = Matrix([[31, 22], [37, 43], [51, 86]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    two_matrix.__str__()
    two_matrix.sum_matrix()  # складываем матрицы одного объекта
