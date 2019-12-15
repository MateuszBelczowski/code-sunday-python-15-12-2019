import sys
import pygame

brazowy = pygame.Color(100, 100, 100)
bialy = pygame.Color(255, 255, 255)
zielony = pygame.Color(37, 168, 20)
init_status = pygame.init()
plansza = pygame.display.set_mode((500, 500))
plansza.fill(bialy)


polozenie_weza = [[10, 10], [20, 10], [30, 10], [40, 10], [50, 10]]


def narysuj_weza():
    plansza.fill(bialy)
    for punkt in polozenie_weza:
        segment = pygame.Rect(punkt[0], punkt[1], 10, 10)
        pygame.draw.rect(plansza, zielony, segment)


narysuj_weza()
pygame.display.flip()

obecny_kierunek = "lewo"

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                obecny_kierunek = "lewo"
            elif event.key == pygame.K_RIGHT:
                obecny_kierunek = "prawo"
            elif event.key == pygame.K_UP:
                obecny_kierunek = "gora"
            elif event.key == pygame.K_DOWN:
                obecny_kierunek = "dol"

    glowa_weza = polozenie_weza[0]
    polozenie_weza.pop()
    if obecny_kierunek == "dol":
        nowa_glowa_weza = [glowa_weza[0], glowa_weza[1] + 10]
    elif obecny_kierunek == "gora":
        nowa_glowa_weza = [glowa_weza[0], glowa_weza[1] - 10]
    elif obecny_kierunek == "prawo":
        nowa_glowa_weza = [glowa_weza[0] + 10, glowa_weza[1]]
    elif obecny_kierunek == "lewo":
        nowa_glowa_weza = [glowa_weza[0] - 10, glowa_weza[1]]
    polozenie_weza = [nowa_glowa_weza] + polozenie_weza

    print(polozenie_weza)
    narysuj_weza()
    pygame.display.flip()




