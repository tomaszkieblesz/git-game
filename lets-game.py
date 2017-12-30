import sys
import pygame
from settings import Settings
from ship import Ship

# Inicjalizacja gry i utworzenie obiektu ekranu
pygame.init()
ai_settings = Settings()
pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
moja_ikona=pygame.image.load('images/ship.bmp')
k=moja_ikona.get_rect()



print(k)
screen=pygame.display.get_surface()
moja_ikona=moja_ikona.convert()
screen.blit(moja_ikona, (20,20))
pygame.display.flip()



# Pętla główna
while True:
    czas=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            print(czas/1000)


    
