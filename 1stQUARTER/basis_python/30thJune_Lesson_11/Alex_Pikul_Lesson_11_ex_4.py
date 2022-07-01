"""
4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class Storage:
    """"Place where our devices are located"""

    def __init__(self, storage_places, used_place=0, storage_lst=[]):
        self.storage_places = storage_places
        self.used_place = used_place
        self.storage_lst = storage_lst

    def add_to_storage(self, device):
        self.used_place += 1
        self.storage_lst.append(device)
        print(f'{device.name} added, in the storage {self.storage_places - int(self.used_place)} places')


class Device:
    """Base class for all devices in the storage"""
    def __init__(self, serial_number, name):
        self.serial_number = serial_number
        self.name = name


class Printer(Device):
    def __init__(self, serial_number, name, color):
        super().__init__(serial_number, name)
        self.color = color

    def print_text(self, text):
        print(f'The {self.color} printer with serial number "{self.serial_number}" printed: "{text}"')


class Fridge(Device):
    def __init__(self, serial_number, name, temperature):
        super().__init__(serial_number, name)
        self.temperature = temperature

    def froze_meal(self, meal):
        print(
            f"All {meal} are frozen (temp minus {self.temperature}) in the fridge with serial "
            f"number \"{self.serial_number}\" ")


class Computer(Device):
    def __init__(self, serial_number, name, kind):
        super().__init__(serial_number, name)
        self.kind = type

    def choose_mode(self, mode):
        if mode == 'on':
            print('Computer is switched on')
        elif mode == 'off':
            print('Computer is switched off')
        else:
            print('Please choose mode "on" or "off"')


if __name__ == '__main__':
    city_storage = Storage(50)  # create storage with 50 places

    my_printer = Printer('001', 'my_printer', 'white')
    my_printer.print_text('Green bus')

    my_fridge = Fridge('001', 'my_fridge', '-300')
    my_fridge.froze_meal('chicken')

    my_computer = Computer('001', 'my_computer', 'on')
    my_computer.choose_mode('off')

    city_storage.add_to_storage(my_printer)





