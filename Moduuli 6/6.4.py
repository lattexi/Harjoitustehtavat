lista = []

syöte = input('Anna luku: ')
def summa(lista):
    return sum(lista)

while syöte != '':
    lista.append(int(syöte))
    syöte = input('Anna luku: ')

print(summa(lista))
