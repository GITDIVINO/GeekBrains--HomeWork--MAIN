"""
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    """Класс 'Worker'"""

    __income = {
        'wage': 100000,
        'bonus%': 25
    }

    def __init__(self, name, surname, position):
        print('___Экземпляр класса "Worker" создан___')
        self.name = name
        self.surname = surname
        self.position = position
        self.income = self.__income


class Position(Worker):
    """Дочерний класс 'Position' наследован от 'Worker'"""

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Зарплата за месяц составляет {self.income['wage']}$ + премия {self.income['wage']//100*25}$")


if __name__ == '__main__':
    alex = Position('Alex', 'Divino', 'Director of directions')
    alex.get_full_name()
    alex.get_total_income()
    print(f'{alex.name} is {alex.position}')
