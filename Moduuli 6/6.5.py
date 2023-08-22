lista = []

syöte = input('Anna luku: ')

def karsi(lista):
    karsittu_lista = [x for x in lista if x % 2 == 0]
    return karsittu_lista

while syöte != '':
    lista.append(int(syöte))
    syöte = input('Anna luku: ')

print("Alkuperäinen lista:", lista)
print("Karsittu lista:", karsi(lista))
