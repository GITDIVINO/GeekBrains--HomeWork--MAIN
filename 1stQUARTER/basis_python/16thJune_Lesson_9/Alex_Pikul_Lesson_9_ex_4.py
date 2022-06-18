"""
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    """ Родительский класс 'Сar' """

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'{self.name} топит {self.speed} км/ч')

    def look_police(self):
        if self.is_police:
            print(f'<<<Фараоны!!! Run, Вася, Run>>>')
        else:
            print(f'Не очкуй, Вася, это обычный {self.name}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print(f'Объект {self.name} класса "TownCar" создан')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')
        if self.speed > 60:
            print(f'Внимание! Превышение скорости на {self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print('Объект "SportCar" создан')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print('Объект "WorkCar" создан')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')
        if self.speed > 40:
            print(f'Внимание! Превышение скорости на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print('-->Woop woop! That’s the sound of da police!<--')


if __name__ == '__main__':
    volkswagen = TownCar(70, 'синий', 'фольц')
    volkswagen.go()
    volkswagen.show_speed()
    volkswagen.turn('вправо')
    volkswagen.stop()
    volkswagen.look_police()

    print('_'*50)

    lada = SportCar(470, 'баклажан', 'седан')
    lada.go()
    lada.show_speed()
    lada.turn('влево')
    lada.stop()
    lada.look_police()

    print('_' * 50)

    reno = WorkCar(45, 'ржавый', 'рено')
    reno.go()
    reno.show_speed()
    reno.turn('со скрипом')
    reno.stop()
    reno.look_police()

    print('_' * 50)

    police = PoliceCar(90, 'сине-белый', 'автозак')
    police.go()
    police.show_speed()
    police.turn('на тебя')
    police.stop()
    police.look_police()

