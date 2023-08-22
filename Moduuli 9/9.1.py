
class Auto:
    def __int__(self, rekisteritunnus, huippunopeus, tämänhetkinennopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

auto = Auto(1, 142)

print (f"{auto.rekisteritunnus} on syntynyt vuonna {auto.huippunopeus}." )