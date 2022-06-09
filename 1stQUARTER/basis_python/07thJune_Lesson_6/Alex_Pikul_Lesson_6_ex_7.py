"""
7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и
новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда
пользователь вводит номер записи, которой не существует.
"""

import sys

with open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\1stQUARTER\basis_python\07thJune_Lesson_6'
          r'\Alex_Pikul_Lesson_6_ex_6\bakery.csv', 'r+', encoding='utf-8') as f:
    psn = f.tell(sys.argv[1])
    f.seek(psn)
    f.write(f'{sys.argv[1]}\n')

    # Не решил, оставлю на потом :))












