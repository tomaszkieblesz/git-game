import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((800, 600))
kw=pygame.Surface((300, 400))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

kw.blit(screen, (10,10))

pygame.display.set_mode()