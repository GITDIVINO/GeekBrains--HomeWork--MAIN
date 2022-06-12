"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
...
|--templates
| |--mainapp
| | |--base.html
| | |--index.html
| |--authapp
| |--base.html
| |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
"""

from pathlib import Path as P
import shutil
import os

pth = P.cwd()
# print(pth)

# shutil.copy(str(pth) + r'\auth-app\base.html', str(pth) + r'\auth-app\auth-app')  # абсолютный путь
# os.replace('auth-app/base.html', 'auth-app/auth-app')  # относительный путь

for element in os.listdir(pth):
    if os.path.isdir(element):
        os.chdir(element)
        # print(f'{element}-------')
        for i in os.listdir(str(pth) + fr'\{element}'):
            # print(i, P.cwd())
            if i[-4:] == 'html':
                shutil.move(str(i), fr'{P.cwd()}\templates')
        os.chdir(pth)
