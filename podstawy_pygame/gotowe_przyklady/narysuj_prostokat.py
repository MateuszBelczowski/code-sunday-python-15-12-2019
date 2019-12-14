import pygame

pygame.init()
plansza = pygame.display.set_mode((500, 500))
kolor = pygame.Color(255, 255, 255)
pygame.draw.rect(plansza, kolor, pygame.Rect(0, 0, 100, 100))
pygame.draw.rect(plansza, kolor, pygame.Rect(50, 50, 150, 150))
pygame.display.flip()
