import os
import sys
import shutil

def delete_project():

    if os.path.exists(str(sys.argv[1])):
        shutil.rmtree(str(sys.argv[1]))

    return print('Стартер удалил структуру проекта')


delete_project()
