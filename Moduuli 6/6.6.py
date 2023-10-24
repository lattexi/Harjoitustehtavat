import math

def laske_yksikkö_hinta(leveys, hinta):
    pinta_ala_cm2 = math.pi * (leveys / 2) ** 2
    pinta_ala_m2 = pinta_ala_cm2 * 10000
    yksikkö_hinta = hinta / pinta_ala_m2
    return yksikkö_hinta

def main():
    print('Syötä ensimmäisen pizzan tiedot: ')
    halkaisija1 = float(input('Halkaisija (cm): '))
    hinta1 = float(input('Hinta (€): '))

    print('Syötä toisen pizzan tiedot: ')
    halkaisija2 = float(input('Halkaisija (cm): '))
    hinta2 = float(input('Hinta (€): '))

    edukkuus1 = laske_yksikkö_hinta(halkaisija1, hinta1)
    edukkuus2 = laske_yksikkö_hinta(halkaisija2, hinta2)

    if edukkuus1 < edukkuus2:
        print('Ensimmäinen pizza on halvempi')
    elif edukkuus2 < edukkuus1:
        print('Toinen pizza on halvempi')

main()
