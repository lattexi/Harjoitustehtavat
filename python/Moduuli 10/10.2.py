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
        self.ykerros = ykerros
        self.hissilk = hissilk

    def aja_hissi(self, hissinum, kerros):
        if 0 <= hissinum < len(self.hissit):
            print(f"Ajetaan hissillä {hissinum + 1} kerrokseen {kerros}.")
            self.hissit[hissinum].siirry_kerrokseen(kerros)
        else:
            print("Annettu hissin numero ei ole kelvollinen.")


talo = Talo(1, 5, 2)

talo.aja_hissi(0, 3)
talo.aja_hissi(1, 4)
