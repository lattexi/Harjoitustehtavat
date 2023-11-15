import random

arpakuutioiden_lukumäärä = int(input('Anna arpakuutioiden lukumäärä: '))

arpakuutioiden_tulos_list = []

summamuuttuja = 0

for noppa in range(arpakuutioiden_lukumäärä):
    heitto_tulos = random.randint(1, 6)
    arpakuutioiden_tulos_list.append(heitto_tulos)

for tulos in arpakuutioiden_tulos_list:
    summamuuttuja += tulos

print(summamuuttuja)

