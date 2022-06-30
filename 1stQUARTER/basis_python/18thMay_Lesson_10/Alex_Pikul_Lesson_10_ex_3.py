"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение,
 уменьшение, умножение и округление до целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод
позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт
строку: *****\n*****\n**. Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, nucleus_num):
        self.nucleus_num = nucleus_num

    def __add__(self, other):
        cell_3 = Cell(self.nucleus_num + other.nucleus_num)
        return cell_3

    def __str__(self):
        return f'{self.nucleus_num} cells'

    def __sub__(self, other):
        if self.nucleus_num >= other.nucleus_num:
            return Cell(self.nucleus_num - other.nucleus_num)
        else:
            return 'residual of cells is less 0'

    def __mul__(self, other):
        cell_3 = Cell(self.nucleus_num * other.nucleus_num)
        return cell_3

    def __floordiv__(self, other):
        cell_3 = Cell(self.nucleus_num // other.nucleus_num)
        return cell_3

    def __truediv__(self, other):
        cell_3 = Cell(self.nucleus_num / other.nucleus_num)
        return cell_3

    def make_order(self, cells_num):
        rows_num = self.nucleus_num // cells_num
        last_row_num = self.nucleus_num % cells_num

        return ('*' * cells_num + '\n') * rows_num + '*' * last_row_num,


if __name__ == '__main__':
    cell_1 = Cell(2500)
    cell_2 = Cell(17)

    print(cell_1 + cell_2)  # addition

    print(cell_1 - cell_2)  # deduction
    print(cell_2 - cell_1)

    print(cell_1 * cell_2)  # multiplication

    print(cell_1 // cell_2)  # division

    print(cell_1 / cell_2)  # division

    print(cell_2.make_order(5))

