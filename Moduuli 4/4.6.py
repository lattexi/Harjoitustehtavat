# Toteutetaan algoritmi Python-koodina

import random

def arvo_piste():
    return random.uniform(-1, 1), random.uniform(-1, 1)

def onko_ympran_sisalla(x, y):
    return x**2 + y**2 < 1

def laske_pi(n):
    osumat = 0
    for _ in range(n):
        x, y = arvo_piste()
        if onko_ympran_sisalla(x, y):
            osumat += 1
    return 4 * osumat / n

N = int(input("Kuinka monta pistettä arvotaan? "))

# Laske ja tulosta π:n likiarvo
pi_likiarvo = laske_pi(N)
print("π:n likiarvo on noin", pi_likiarvo)
