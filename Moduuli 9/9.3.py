class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, muutos):
        uusinopeus = self.tämänhetkinennopeus + muutos
        self.tämänhetkinennopeus = max(0, min(uusinopeus, self.huippunopeus))

    def kulje(self, tunnit):
        matka = self.tämänhetkinennopeus * tunnit
        self.kuljettumatka += matka



auto = auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kulje(1)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tämänhetkinennopeus} km/h")

auto.kiihdytä(70)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tämänhetkinennopeus} km/h")

auto.kiihdytä(50)
auto.kulje(1)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tämänhetkinennopeus} km/h")

auto.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.tämänhetkinennopeus} km/h")

print (f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.tämänhetkinennopeus}, {auto.kuljettumatka}")