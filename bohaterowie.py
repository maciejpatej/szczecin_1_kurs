import json

with open('heroes.json', 'r') as f:
    data = json.load(f)

# print(data)
odczyt1 = data['secretBase']
odczyt2 = data['members'][0]['powers'][2]
lista = []
for index, wartosc in enumerate(data['members']):
    print(index, wartosc)
