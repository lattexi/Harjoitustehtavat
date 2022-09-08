luku = input('Anna luku: ')

suurin_luku = float(luku)
pienin_luku = float(luku)

while luku != '':
    if float(luku) > suurin_luku:
        suurin_luku = float(luku)

    elif float(luku) < pienin_luku:
        pienin_luku = float(luku)

    luku = input('Anna luku: ')

print('Suurin luku: ',suurin_luku)
print('Pienin luku: ', pienin_luku)