import pygame
import sys

pygame.init()

window=pygame.display.set_mode((800, 600))


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.display.update()
