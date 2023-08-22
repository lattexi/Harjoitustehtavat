lista = []

syöte = input('Anna luku: ')

while syöte != '':
    lista.append(int(syöte))
    syöte = input('Anna luku: ')

lista.sort(reverse=True)

for i in range(4):
    print(lista[i])
