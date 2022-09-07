import random

tahkot = int(input('Tahkot: '))

def nopanheitto(tahkot):
    random_silmäluku = random.randint(1, tahkot)
    if(random_silmäluku == 6):
        print(random_silmäluku)
    else:
        print(random_silmäluku)
        nopanheitto(tahkot)
    return

print(nopanheitto(tahkot))