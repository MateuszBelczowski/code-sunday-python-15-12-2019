import pygame

pygame.init()
czcionka = pygame.font.SysFont('monaco', 72)
kolor = pygame.Color(100, 100, 100)
plansza = pygame.display.set_mode((1000, 500))
napis = czcionka.render("Warsztaty Code Sunday", True, kolor)
plansza.blit(napis, (0, 0))
pygame.display.flip()
