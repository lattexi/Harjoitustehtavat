import random

def nopanheitto():
    random_silmäluku = random.randint(1, 6)
    if(random_silmäluku > 5):
        print(random_silmäluku)
    else:
        print(random_silmäluku)
        nopanheitto()
    return

print(nopanheitto())
