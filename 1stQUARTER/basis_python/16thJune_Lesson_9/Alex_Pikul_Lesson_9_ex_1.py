"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    """Класс светофор работает в 2х режимах: ручной и автоматический"""

    def __init__(self):
        print('___Экземпляр класса "TrafficLight" создан___')
        self.__light_color = ['красный', 'жёлтый', 'зелённый']
        self.a = 0

    def running(self):
        print(f'Светофор запущен, сейчас {self.__light_color[0]} свет')

    def switch_color(self):
        if self.a == 0:
            self.a += 1
            print(f'---> Переключили светофор вручную на {self.__light_color[self.a]} свет')
        elif self.a == 1:
            self.a += 1
            print(f'---> Переключили светофор вручную на {self.__light_color[self.a]} свет')
        elif self.a == 2:
            self.a = 0
            print(f'---> Переключили светофор вручную на {self.__light_color[self.a]} свет')

    def auto_switch_color(self):
        print(f'---Внивание! Автоматический режим переключения активирован---\nСейчас {self.__light_color[0]} свет')
        while True:
            if self.a == 0:
                self.a += 1
                print(f'Переключение на {self.__light_color[self.a]} свет через 7 секунд')
                time.sleep(7)
                print(f'---> Светофор автоматически переключён на {self.__light_color[self.a]} свет')
            elif self.a == 1:
                self.a += 1
                print(f'Переключение на {self.__light_color[self.a]} свет через 2 секунды')
                time.sleep(2)
                print(f'---> Светофор автоматически переключён на {self.__light_color[self.a]}')
            elif self.a == 2:
                self.a = 0
                print(f'Переключение на {self.__light_color[self.a]} свет через 5 секунды')
                time.sleep(5)
                print(f'---> Светофор автоматически переключён на {self.__light_color[self.a]}')


if __name__ == '__main__':
    new_trafficlight = TrafficLight()  # создаём экземпляр класса TrafficLight
    new_trafficlight.running()
    while True:
        usr_chc = int(input('1 - Ручное переключение\n2 - Автоматическое переключение\nВведите действие: '))
        if usr_chc == 1:
            new_trafficlight.switch_color()
        elif usr_chc == 2:
            new_trafficlight.auto_switch_color()
