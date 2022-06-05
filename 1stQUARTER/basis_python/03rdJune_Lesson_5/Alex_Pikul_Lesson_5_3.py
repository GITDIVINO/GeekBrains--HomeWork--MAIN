"""
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
генератор даст эффект.
"""


def make_gen_from_2lst(lst_1, lst_2):
    """Функция принимает 2 листа и возвращает картежи вида <lst_1>, <lst_2>"""
    i = 0
    while i < len(lst_1) and i < len(lst_2):
        yield lst_1[i], lst_2[i]
        i += 1
    while i < len(lst_1):
        yield lst_1[i], None
        i += 1


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Данила']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

#   проверяем случай (<tutor>, None)
for i in make_gen_from_2lst(tutors, klasses):
    print(i, type(i))

#   присваиваем генератор переменной и вызываем до истощения
lst_gen = make_gen_from_2lst(tutors, klasses)
# print(lst_gen, next(lst_gen), next(lst_gen), next(lst_gen), next(lst_gen), next(lst_gen), next(lst_gen),
#       next(lst_gen), next(lst_gen), next(lst_gen), next(lst_gen), sep='\n')

#   или
for i in range(10):
    print(next(lst_gen))
