lista = [1, 3, 5, 6, "kot", "pies", True, False]
print(lista)

for element in lista:
    print(element)

print(lista[0])
lista[4] = "kaczka"
print(lista)

lista_liczb = [1, 2, 3]
lista_zwierzat = ['kot', 'pies']

nowa_lista = lista_liczb + lista_zwierzat
print(nowa_lista)

nowa_lista.append("kon")
print(nowa_lista)
zwierze = nowa_lista.pop()
print(zwierze)
print(nowa_lista)

lista_zagniezdzona = [[10, 20], [30, 40], [50, 60]]
print(len(lista_zagniezdzona[-1]))
