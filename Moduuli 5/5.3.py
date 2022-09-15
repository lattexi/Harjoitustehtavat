import math

luku = int(input('Anna luku: '))

jaollinen = False

if luku != 2 and not luku % 2:
    jaollinen = True

for i in range(2, int(math.sqrt(luku)) + 1,):
    if luku % i == 0:
        jaollinen = True
        break

if jaollinen:
    print('Ei ole alkuluku')
else:
    print('On alkuluku')
