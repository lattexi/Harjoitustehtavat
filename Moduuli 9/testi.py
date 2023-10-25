class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0  # Asetetaan automaattisesti nollaksi
        self.kuljettu_matka = 0  # Asetetaan automaattisesti nollaksi

    def __str__(self):
        return f'Rekisteritunnus: {self.rekisteritunnus}\nHuippunopeus: {self.huippunopeus} km/h\nTämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h\nKuljettu matka: {self.kuljettu_matka} km'

    def kiihdyta(self, muutos):
        # Lasketaan uusi nopeus, mutta rajoitetaan se välille 0 - huippunopeus
        uusi_nopeus = self.tamanhetkinen_nopeus + muutos
        self.tamanhetkinen_nopeus = max(0, min(uusi_nopeus, self.huippunopeus))

def main():
    # Luodaan uusi auto
    auto = Auto("ABC-123", 142)

    # Tulostetaan auton kaikki ominaisuudet
    print(auto)
    print("")  # Tyhjä rivi tulosteiden välissä

    # Kiihdytetään autoa
    auto.kiihdyta(30)
    print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")

    auto.kiihdyta(70)
    print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")

    auto.kiihdyta(50)  # Yrittää ylittää huippunopeuden
    print(f"Auton nopeus kiihdytyksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")

    # Hätäjarrutus
    auto.kiihdyta(-200)  # Yrittää alittaa miniminopeuden
    print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")


if __name__ == "__main__":
    main()
