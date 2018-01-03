import pygame


pygame.init()

window=pygame.display.set_mode((800,600), 0, 32)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for x in range(100):
        random_color= (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
        random_pos=(random.randint(0,800), random.randint(0,600))
        window.set_at(random_pos, random_color)
        pygame.display.flip()

#Ok spróbujmy jak sie pracuje na gałęzi PRO




