kuha_str = input('Anna kuhan pituus: ')
kuha = float(kuha_str)

if kuha<37:
    print('Kuha on alimittainen')
    print(f'Kuhan pituudesta puuttuu: {37-kuha}cm')
else:
    print('Kuhan voi pitää')