leiviskä_str = input('Anna leiviskät: ')
naula_str = input('Anna naulat: ')
luoti_str = input('Anna luodit: ')

leiviskä = float(leiviskä_str)
naula = float(naula_str)
luoti = float(luoti_str)

kg = (0.0133*luoti + 0.0133*32*naula + 0.0133*32*20*leiviskä)

print(f'{kg:.0f}')
