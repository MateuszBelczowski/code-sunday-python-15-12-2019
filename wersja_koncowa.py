import pygame
import sys
import time
import random

# Pygame Init
init_status = pygame.init()
if init_status[1] > 0:
    print("(!) Had {0} initialising errors, exiting... ".format(init_status[1]))
    sys.exit()
else:
    print("(+) Pygame initialised successfully ")

# Play Surface
rozmiar = szerokosc, wysokosc = 640, 320
plansza = pygame.display.set_mode(rozmiar)
pygame.display.set_caption("Snake CodeSunday")


# Colors
czerwony = pygame.Color(255, 0, 0)
zielony = pygame.Color(0, 255, 0)
czarny = pygame.Color(0, 0, 0)
bialy = pygame.Color(255, 255, 255)
brazowy = pygame.Color(165, 42, 42)

kontroler_predkosci = pygame.time.Clock()

# Game settings
przesuniecie = 10
glowa_weza = [100, 50]
waz = [[100, 50], [90, 50], [80, 50]]
pozycja_jedzenia = [400, 50]
wstaw_nowe_jedzenie = True
PRAWO = 'PRAWO'
LEWO = 'LEWO'
GORA = 'GORA'
DOL = 'DOL'
kierunek = PRAWO
nowy_kierunek = ''
wynik = 0


def koniec_gry():
    czcionka = pygame.font.SysFont('monaco', 72)
    napis = czcionka.render("Koniec gry", True, czerwony)
    pozycja_napisu = (320, 25)
    plansza.blit(napis, pozycja_napisu)
    pokaz_wynik(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


# Show Score
def pokaz_wynik(choice=1):
    czcionka = pygame.font.SysFont('monaco', 32)
    napis = czcionka.render("Wynik  :  {0}".format(wynik), True, czarny)
    if choice == 1:
        pozycja_napisu = (80, 10)
    else:
        pozycja_napisu = (320, 100)
    plansza.blit(napis, pozycja_napisu)


def wygeneruj_nowa_pozycje():
    return [random.randrange(1, szerokosc // 10) * przesuniecie, random.randrange(1, wysokosc // 10) * przesuniecie]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                nowy_kierunek = PRAWO
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                nowy_kierunek = LEWO
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                nowy_kierunek = GORA
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                nowy_kierunek = DOL
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if nowy_kierunek == PRAWO and kierunek != LEWO:
        kierunek = nowy_kierunek
    elif nowy_kierunek == LEWO and kierunek != PRAWO:
        kierunek = nowy_kierunek
    elif nowy_kierunek == GORA and kierunek != DOL:
        kierunek = nowy_kierunek
    elif nowy_kierunek == DOL and kierunek != GORA:
        kierunek = nowy_kierunek

    if kierunek == PRAWO:
        glowa_weza[0] += przesuniecie
    elif kierunek == LEWO:
        glowa_weza[0] -= przesuniecie
    elif kierunek == DOL:
        glowa_weza[1] += przesuniecie
    elif kierunek == GORA:
        glowa_weza[1] -= przesuniecie

    waz.insert(0, list(glowa_weza))
    if glowa_weza == pozycja_jedzenia:
        wstaw_nowe_jedzenie = False
        wynik += 1
    else:
        waz.pop()
    if wstaw_nowe_jedzenie is False:
        pozycja_jedzenia = wygeneruj_nowa_pozycje()
        wstaw_nowe_jedzenie = True
    plansza.fill(bialy)
    for segment in waz:
        pygame.draw.rect(plansza, zielony, pygame.Rect(segment[0], segment[1], przesuniecie, przesuniecie))
    pygame.draw.rect(plansza, brazowy, pygame.Rect(pozycja_jedzenia[0], pozycja_jedzenia[1], przesuniecie, przesuniecie))

    # Zderzenie ze ścianą
    if glowa_weza[0] >= szerokosc or glowa_weza[0] < 0:
        koniec_gry()
    if glowa_weza[1] >= wysokosc or glowa_weza[1] < 0:
        koniec_gry()

    # Zderzenie z samym soba
    for segment in waz[1:]:
        if glowa_weza == segment:
            koniec_gry()
    pokaz_wynik()
    pygame.display.flip()
    kontroler_predkosci.tick(10)
