import os
import yaml
from pprint import pprint


def create_project():

    with open('config.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    pprint(data)

    for key in data:
        if not os.path.exists(key):
            os.mkdir(key)
            pth = os.getcwd()
            if data[key] is not None:
                for k in data[key]:
                    if k[-1:] == 'y':
                        os.chdir(key)
                        with open(f'{k}', 'a', encoding='utf-8') as f:
                            f.writelines('file created')
                        os.chdir(pth)
                    elif k[-1:] == 'l':
                        os.chdir(key)
                        with open(f'{k}', 'a', encoding='utf-8') as f:
                            f.writelines('file created')
                        os.chdir(pth)
                    else:
                        os.chdir(key)
                        os.mkdir(k)
                        os.chdir(pth)


if __name__ == "__main__":
    create_project()
