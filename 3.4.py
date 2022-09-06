vuosi = int(input('Anna vuosi: '))

on_karkausvuosi = False

if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        on_karkausvuosi = True

elif vuosi % 4 == 0:
    on_karkausvuosi = True

if on_karkausvuosi:
    print('Vuosi on karkausvuosi')
else:
    print('Vuosi ei ole karkausvuosi')
