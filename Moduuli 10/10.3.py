class Hissi:
    def __init__(self, akerros, ykerros):
        self.kerros = akerros
        self.akerros = akerros
        self.ykerros = ykerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros != kohde_kerros:
            if self.kerros < kohde_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.ykerros > self.kerros:
            self.kerros += 1
            print(f'Hissi on nyt kerroksessa {self.kerros}')
        else:
            print(f'Hissi on jo ylimmässä kerroksessa')

    def kerros_alas(self):
        if self.akerros < self.kerros:
            self.kerros -= 1
            print(f'Hissi on nyt kerroksessa {self.kerros}')
        else:
            print(f'Hissi on jo alimmassa kerroksessa')


class Talo:
    def __init__(self, akerros, ykerros, hissilk):
        self.hissit = [Hissi(akerros, ykerros) for _ in range(hissilk)]
        self.akerros = akerros

    def aja_hissi(self, hissinum, kerros):
        if 0 <= hissinum < len(self.hissit):
            print(f"Ajetaan hissillä {hissinum} kerrokseen {kerros}.")
            self.hissit[hissinum].siirry_kerrokseen(kerros)
        else:
            print("Annettu hissin numero ei ole kelvollinen.")

    def palohälytys(self):
        print("PALOHÄLYTYS! Kaikki hissit pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.akerros)


talo = Talo(1, 5, 2)
talo2 = Talo(1, 10, 4)

talo.aja_hissi(1, 3)
talo.aja_hissi(1, 4)
talo.palohälytys()

talo2.aja_hissi(0, 5)
talo2.aja_hissi(3, 9)
talo2.palohälytys()