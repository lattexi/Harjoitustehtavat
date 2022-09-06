gender = input('Anna sukupuoli: ')
blood = float(input('Anna hemoglobiiniarvo: '))

if gender == 'mies':
    if blood < 117:
        print('Hemoglobiini on alhainen')
    elif blood > 175:
        print('Hemoglobiini on korkea')
    else:
        print('Hemoglobiini on normaali')

elif gender == 'nainen':
    if blood < 134:
        print('Hemoglobiini on alhainen')
    elif blood > 195:
        print('Hemoglobiini on korkea')
    else:
        print('Hemoglobiini on normaali')
