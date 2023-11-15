import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

    def __str__(self):
        return f'{self.rekisteritunnus}\t\t\t{self.huippunopeus}\t\t\t\t\t{self.tämänhetkinennopeus}\t\t\t\t{self.kuljettumatka}'

    def kiihdytä(self, muutos):
        uusinopeus = self.tämänhetkinennopeus + muutos
        self.tämänhetkinennopeus = max(0, min(uusinopeus, self.huippunopeus))

    def kulje(self, tunnit):
        matka = self.tämänhetkinennopeus * tunnit
        self.kuljettumatka += matka

autot = []
for i in range(10):
    auto = Auto("ABC-" + str(i+1), random.randint(100, 200))
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)  # Arvotaan nopeuden muutos
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)  # Liikutaan yhden tunnin verran

        if auto.kuljettumatka >= 10000000:
            kilpailu_kaynnissa = False
            break

print("Rekisterinumero\tHuippunopeus (km/h)\tNopeus (km/h)\tMatka (km)")


for auto in autot:
    print(auto)