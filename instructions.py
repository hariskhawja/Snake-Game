import pygame
from functions import textDisplay
from config import Config

def instructions(screen, font, titleFont):
    fpsClock = pygame.time.Clock()

    while True:
        screen.fill([0, 0, 0])
        text = ["Instructions", "1. Use arrow keys to move snake", "2. Eat apples to increase in length and gain points", "3. Do not hit tail or walls"]
        
        for key, value in enumerate(text): 
            f = font
            if key == 0: f = titleFont
                
            textDisplay(value, f, (50, 100 + (key*50)), screen, "l")

        menu = pygame.draw.rect(screen, Config['colors']['blue'], (350, 500, 100, 30))
        textDisplay("MENU", font, [400, 515], screen, "c")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if menu.collidepoint(pygame.mouse.get_pos()): return 0

            if event.type == pygame.QUIT: return 9

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])