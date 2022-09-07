import random

tahkot = int(input('Tahkot: '))

def arvoHeitto(tahkot):
    return random.randint(1, tahkot)

def nopanheitto(tahkot):
    random_silmäluku = arvoHeitto(tahkot)
    while(random_silmäluku < tahkot):
        print(random_silmäluku)
        random_silmäluku = arvoHeitto(tahkot)

    print(random_silmäluku)

nopanheitto(tahkot)