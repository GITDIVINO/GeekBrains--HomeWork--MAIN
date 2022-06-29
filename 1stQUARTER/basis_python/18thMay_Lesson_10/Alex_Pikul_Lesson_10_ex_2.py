"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных. Выполнить общий подсчёт расхода ткани. Проверить на
практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
"""

from abc import ABC
from abc import abstractmethod


class clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod  # abstract method, should be redefined
    def how_much(self):
        pass


class coat(clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def calc_cunsumption(self):
        return f'{self.v // 6.5 + 0.5} m fabric spent on {self.name} coat'

    def how_much(self):
        print('It`s very expensive')


class suit(clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def calc_consumption(self):
        return f'{2 * self.h + 0.3} m fabric spent on {self.name} suit'

    def how_much(self):
        print('It`s very cheap')


if __name__ == '__main__':
    coat_1 = coat('GUCHI', 43)
    # print(coat_1.calc_consumption())    # without @property - 6.5 m fabric spent on GUCHI coat
    print(coat_1.calc_cunsumption)  # @property is working - 6.5 m fabric spent on GUCHI coat
    coat_1.how_much()  # abstract method

    suit_1 = suit('BOSS', 180)
    # print(suit_1.calc_consumption())    # without @property - 360.3 m fabric spent on BOSS suit
    print(suit_1.calc_consumption)  # @property is working - 360.3 m fabric spent on BOSS suit
    suit_1.how_much()  # abstract method
