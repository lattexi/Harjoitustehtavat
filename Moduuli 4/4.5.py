tries = 0

while tries < 5:
    user = input('Anna käyttäjätunnus: ')
    password = input('Anna salasana: ')
    if user == 'python':
        if password == 'root':
            print('Tervetuloa')
            break
        else:
            tries += 1
    else:
        tries += 1

if tries >= 5:
    print('Pääsy evätty')
