import random

def arvoHeitto():
    return random.randint(1, 6)

def nopanheitto():
    random_silmäluku = arvoHeitto()
    while(random_silmäluku < 6):
        print(random_silmäluku)
        random_silmäluku = arvoHeitto()

    print(random_silmäluku)

nopanheitto()
