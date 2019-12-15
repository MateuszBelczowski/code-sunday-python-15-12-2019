import sys
import pygame
import random

brazowy = pygame.Color(100, 100, 100)
bialy = pygame.Color(255, 255, 255)
zielony = pygame.Color(37, 168, 20)
init_status = pygame.init()
plansza = pygame.display.set_mode((500, 500))
plansza.fill(bialy)

kontroler_predkosci = pygame.time.Clock()

polozenie_weza = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]]


def narysuj_weza():
    plansza.fill(bialy)
    for punkt in polozenie_weza:
        segment = pygame.Rect(punkt[0], punkt[1], 10, 10)
        pygame.draw.rect(plansza, zielony, segment)


def wylosuj_polozenie_owocu():
    rand_x = random.randint(0, 50) * 10
    rand_y = random.randint(0, 50) * 10
    return rand_x, rand_y


def narysuj_owoc(x, y):
    owoc = pygame.Rect(x, y, 10, 10)
    pygame.draw.rect(plansza, brazowy, owoc)


narysuj_weza()
polozenie_owocu_x, polozenie_owocu_y = wylosuj_polozenie_owocu()
narysuj_owoc(polozenie_owocu_x, polozenie_owocu_y)
pygame.display.flip()

obecny_kierunek = "lewo"

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT and obecny_kierunek != "prawo":
                obecny_kierunek = "lewo"
            elif event.key == pygame.K_RIGHT and obecny_kierunek != "lewo":
                obecny_kierunek = "prawo"
            elif event.key == pygame.K_UP and obecny_kierunek != "dol":
                obecny_kierunek = "gora"
            elif event.key == pygame.K_DOWN and obecny_kierunek != "gora":
                obecny_kierunek = "dol"

    kontroler_predkosci.tick(10)
    glowa_weza = polozenie_weza[0]
    if obecny_kierunek == "dol":
        nowa_glowa_weza = [glowa_weza[0], glowa_weza[1] + 10]
    elif obecny_kierunek == "gora":
        nowa_glowa_weza = [glowa_weza[0], glowa_weza[1] - 10]
    elif obecny_kierunek == "prawo":
        nowa_glowa_weza = [glowa_weza[0] + 10, glowa_weza[1]]
    elif obecny_kierunek == "lewo":
        nowa_glowa_weza = [glowa_weza[0] - 10, glowa_weza[1]]
    polozenie_weza = [nowa_glowa_weza] + polozenie_weza

    if glowa_weza[0] == polozenie_owocu_x and glowa_weza[1] == polozenie_owocu_y:
        polozenie_owocu_x, polozenie_owocu_y = wylosuj_polozenie_owocu()
    else:
        polozenie_weza.pop()

    print(polozenie_weza)
    narysuj_weza()
    narysuj_owoc(polozenie_owocu_x, polozenie_owocu_y)
    pygame.display.flip()




