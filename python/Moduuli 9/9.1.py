
class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0



auto = auto("ABC-123", 142)

print (f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.tämänhetkinennopeus}, {auto.kuljettumatka}")