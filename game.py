import pygame
from config import Config

def game(screen):
    quitVar = True
    fpsClock = pygame.time.Clock()

    while quitVar:
        screen.fill([0, 0, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])
    
