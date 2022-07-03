"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import re


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod    # this def only devide exact date format, without validation or convertation
    def divide_date(cls, date):
        splited_date = date.split('-')
        day = int(splited_date[0])
        month = int(splited_date[1])
        year = int(splited_date[2])
        return day, month, year

    @staticmethod
    def validate_date(date):
        VALID_DATE = re.compile(r'[0-3]\d-[0-1]\d-2022')
        if not VALID_DATE.match(date):
            return f'Date {date} is NOT valid'
        return f'Date {date} is valid'


if __name__ == '__main__':
    # any_date = input('Please inpute date in format "day-month-year": ')   # in case it`s needed for user` data
    any_date = '11-05-1993'
    any_date_2 = '11-05-2022'
    print(Date.divide_date(any_date))   # can call without creating an object

    print(Date.validate_date(any_date))    # can call without creating an object
    print(Date.validate_date(any_date_2))













