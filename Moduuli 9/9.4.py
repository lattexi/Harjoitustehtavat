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


autot = []


