import json

# full dict of the vessel with parameters for counting of freight
vessels = {
    'nordborg': {
        'consumption': 6.5,
        'speed': 10.5,
        'capacity': 210000},

    'ostborg': {
        'consumption': 6.5,
        'speed': 10.5,
        'capacity': 205000},

    'sydborg': {
        'consumption': 6.5,
        'speed': 10.5,
        'capacity': 205000},

    'westborg': {
        'consumption': 6.5,
        'speed': 10.5,
        'capacity': 205000},

    'bergfjord': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 172000},

    'tucana': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 185000},

    'aerandir': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 185000},

    'avalon': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 185000},

    'ankie': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'emma': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'jolyn': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'leonie': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'heyn': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'mila': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'robijn': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'ruyter': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'sprinter': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'speyk': {
        'consumption': 6,
        'speed': 10.5,
        'capacity': 174000},

    'andrea': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'carolina': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'noorderliht': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'egon w': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'elke w': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'marietje hester': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'merel v': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'susanne': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'panta rhei': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'kelt': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'cristina': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'adamas': {
        'consumption': 5,
        'speed': 10,
        'capacity': 160000},

    'alana evita': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'cito': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'helenic': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'hekla': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'hestia': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'hydra': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'jade': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'priscilla': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},

    'zeeland': {
        'consumption': 5,
        'speed': 10,
        'capacity': 158985},
}

# full list of the vessel as per contract
vessels_lst = []
for vessel in vessels:
    vessels_lst.append(vessel)

# creating json file to speed up the programm
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(vessels, outfile)

