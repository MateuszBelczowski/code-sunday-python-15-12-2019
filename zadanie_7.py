"""
Napisz program, który:

pobierze od użytkownika 5 dowolnych wyrazów i utworzy z nich listę
posortuje utworzoną listę
wyświetli pierwszy element listy
zapyta użytkownika o kolejny wyraz, który ma nadpisać wyświetlony element
wyświetli elementy listy w celu potwierdzenia, że dokonano modyfikacji
"""

lista = []
for i in range(5):
    wyraz = input("Podaj wyraz ->")
    lista.append(wyraz)
print(lista)
lista.sort()

print(lista[0])

lista[0] = input("Podaj nowy wyraz ->")
print(lista)

