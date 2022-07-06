import json
from pprint import pprint

vessels_dict = {}

with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        vessels_dict[i] = data[i]

# pprint(vessels_dict)

vessel_name = 'adamas'

if vessel_name in vessels_dict:
    a_ = []
    for i in vessels_dict[vessel_name]:
        a_.append(f'{i} - {vessels_dict[vessel_name][i]}')

    print(vessel_name, a_)

