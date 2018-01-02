import pygame
import sys

pygame.init()
window = pygame.display.set_mode((600, 400), 0, 32)
screen=pygame.display.get_surface()
kwadrat=pygame.image.load('images/ship.bmp').convert()

kwadrat.set_alpha(10)
screen.fill((120,120,120))

screen.blit(kwadrat, (20,20))
pygame.display.flip()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                screen.fill((120,120,120))
                kwadrat.set_alpha(15)
                screen.blit(kwadrat, (20,20))

                pygame.display.update()




