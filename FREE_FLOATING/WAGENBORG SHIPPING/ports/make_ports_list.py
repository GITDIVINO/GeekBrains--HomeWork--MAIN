import json

# full dict of the vessel with parameters for counting of freight
ports = {
    'Kaliningrad': {
        'st malo': 992,
        'le legue': 1001},

    'Klaipeda': {
        'st malo': 1064,
        'le legue': 1064}
}

# full list of the vessel as per contract
ports_lst = []
for port in ports:
    ports_lst.append(port)

# creating json file to speed up the programm
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(ports, outfile)