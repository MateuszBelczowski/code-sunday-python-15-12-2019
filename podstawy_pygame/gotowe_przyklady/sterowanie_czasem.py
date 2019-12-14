import datetime
import pygame

# Pygame Init
init_status = pygame.init()
kontroler_predkosci = pygame.time.Clock()
plansza = pygame.display.set_mode((500, 500))
zdarzenia = []
while True:
    for event in pygame.event.get():
        zdarzenia.append(event)
    print(f"Czas: {datetime.datetime.now()}, liczba zdarzen: {len(zdarzenia)}")
    kontroler_predkosci.tick(0.1)
