import math

leiviskä = float(input('Anna leiviskät: '))
naula = float(input('Anna naulat: '))
luoti = float(input('Anna luodit: '))

kg = (0.0133 * luoti + 0.0133 * 32 * naula + 0.0133 * 32 * 20 * leiviskä)
g = kg % 1

print(f'{math.floor(kg)} kg ja {g*1000:.2f} g')
