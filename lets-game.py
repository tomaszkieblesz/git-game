import matplotlib, sys

import requests

import pygame

print(pygame.__version__)
screen = pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit(0)

    # Rysowanie
    pygame.draw.rect(screen, (20, 100, 255), pygame.Rect(10, 50, 200, 100))
    pygame.display.flip()
