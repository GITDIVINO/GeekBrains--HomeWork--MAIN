"""
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    """Родительский класс 'Stationery'"""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект ручка класса "канцелярская принадлежность" создан---')

    def draw(self):
        print(f'"{self.title}" - написано ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект карандаш класса "канцелярская принадлежность" создан---')

    def draw(self):
        print(f'"{self.title}" - написано карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект маркер класса "канцелярская принадлежность" создан---')

    def draw(self):
        print(f'"{self.title}" - написано маркером')


if __name__ == '__main__':
    pen = Pen('Халк как огонь, Тор как вода')
    pen.draw()

    print('_'*30)

    pencil = Pencil('Скорее мы оба как огонь')
    pencil.draw()

    print('_' * 30)

    handle = Handle('Халк как пылающий огонь, Тор как тлеющий огонь')
    handle.draw()
