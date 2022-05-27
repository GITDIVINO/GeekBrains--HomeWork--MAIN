'''1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн
<h> час <m> мин <s> сек.

Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек

Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для
нескольких значений продолжительности, будет ли тут полезен список?'''

# прописываем функцию принимающая на вход список
import random


def make_better_view(duration):
    if duration <= 60:
        return f'{duration} сек'
    elif 60 < duration <= 3600:
        min = duration // 60
        sec = duration - 60 * min
        return f'{min} мин {sec} сек'
    elif 3600 < duration <= 86400:
        hour = duration // 3600
        min = (duration - 3600 * hour) // 60
        sec = duration - 3600 * hour - 60 * min
        return f'{hour} час {min} мин {sec} сек'
    else:
        day = duration // 86400
        hour = (duration - 86400 * day) // 3600
        min = (duration - 86400 * day - 3600 * hour) // 60
        sec = duration - 86400 * day - 3600 * hour - 60 * min
        return f'{day} дн {hour} час {min} мин {sec} сек'


# создаём спиок рандомных значений в секундах
duration_lst = [random.randint(1, 500000) for i in range(20)]

# проходим по списку значений с помощью цикла fot, вызывая функцию
for duration in duration_lst:
    print(f'Переводим {duration} сек: {make_better_view(duration)}')
