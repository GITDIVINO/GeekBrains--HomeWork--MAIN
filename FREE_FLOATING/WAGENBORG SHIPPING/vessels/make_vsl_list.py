import json

# full dict of the vessel with parameters for counting of freight
vessels = {
    'adamas': {
        'consumption': 5,
        'speed': 10.5,
        'capacity': 160000},
    'ankie': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 160000},
}

# full list of the vessel as per contract
vessels_lst = []
for key in vessels:
    vessels_lst.append(key)

# creating json file to speed up the programm
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(vessels, outfile)

