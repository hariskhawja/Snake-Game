import pygame
from functions import textDisplay, textY
from config import Config

def credits(screen, font, titleFont):
    fpsClock = pygame.time.Clock()

    while True:
        screen.fill([0, 0, 0])
        text = ["Credits", "Designer: Haris Khawja", "Supervisors: Coach Asad, Coach Saeesh", "Company: Zebra Robotics", "Language: Python 3, Pygame", "Completion Date: 2023-04-28"]
        
        for key, value in enumerate(text): 
            f = font
            if key == 0: f = titleFont
                
            textDisplay(value, f, (50, 100 + (key*50)), screen, "l")

        menu = pygame.draw.rect(screen, Config['colors']['blue'], (350, 500, 100, 30))
        textDisplay("MENU", font, [400, textY(500)], screen, "c")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if menu.collidepoint(pygame.mouse.get_pos()): return 0

            if event.type == pygame.QUIT: return 9

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])