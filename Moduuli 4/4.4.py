import random

random_luku = random.randint(1, 10)
arvattu_luku = int(input('Arvaa luku: '))

while arvattu_luku is not random_luku:
    if arvattu_luku < random_luku:
        print('Liian pieni arvaus')
        arvattu_luku = int(input('Arvaa luku: '))

    elif arvattu_luku > random_luku:
        print('liian suuri arvaus')
        arvattu_luku = int(input('Arvaa luku: '))

print('Oikein!')






