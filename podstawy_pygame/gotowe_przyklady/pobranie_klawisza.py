import pygame

# Pygame Init
init_status = pygame.init()
plansza = pygame.display.set_mode((500, 500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(f"ID przycisku to {event.key}")
