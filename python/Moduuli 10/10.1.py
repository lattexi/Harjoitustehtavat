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


h = Hissi(1, 5)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

