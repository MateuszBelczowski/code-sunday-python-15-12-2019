import random

wylosowana_liczba = random.randint(1, 101)  # wygeneruj liczbę z zakresu 1-100
licznik_prob = 0
while True:
    strzal = int(input("Podaj liczbę z zakresu: 1-100 ->"))
    licznik_prob += 1
    if strzal > wylosowana_liczba:
        print("Za duża liczba")
    elif strzal < wylosowana_liczba:
        print("Za mała liczba")
    else:
        print(f"Zgadłeś, liczba to {wylosowana_liczba}, potrzebowałeś na to {licznik_prob} strzałów")
        break



    # pobierz liczbe od uzytkownika
    # sprawdz czy jest wieksza/mniejsza/rowna
    # poinformuj o wyniku
    # zakoncz jezeli jest rowna
    pass
