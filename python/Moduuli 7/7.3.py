vaihtoehto = input('Jos haluat syöttää lentoaseman paina 1\n'
                   'Jos haluat hakea lentoaseman paina 2\n'
                   'Jos haluat lopettaa paina ENTER\n')

lentoasemat = {}

while vaihtoehto != '':
    if int(vaihtoehto) == 1:
        icao = input('Syötä ICAO koodi: \n')
        lentoasema = input('Syötä lentoaseman nimi: \n')
        lentoasemat[icao] = lentoasema

    elif int(vaihtoehto) == 2:
        haku = input('Syötä ICAO koodi: \n')
        if haku in lentoasemat:
            print(lentoasemat[haku])
        else:
            print('Lentoasemaa ei löydy')

    vaihtoehto = input('Jos haluat syöttää lentoaseman paina 1\n'
                       'Jos haluat hakea lentoaseman paina 2\n'
                       'Jos haluat lopettaa paina ENTER\n')
