nimet = set()

nimi = input('Syötä nimi: ')
nimet.add(nimi)

while nimi != '':
    nimi = input('Syötä nimi: ')
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
        nimet.add(nimi)

    else:
        print('Uusi nimi')
        nimet.add(nimi)