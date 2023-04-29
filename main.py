import pygame
from menu import menu
from game import game
from instructions import instructions
from credits import credits
from config import Config

pygame.init()
pygame.display.set_caption("Snake Game")

page = 0
highscore = 0

screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

font = pygame.font.SysFont(Config['game']['font'], Config['game']['fontSize'])
titleFont = pygame.font.SysFont(Config['game']['font'], Config['game']['titleSize'])

while True:
    if page == 0: 
        page, fps = menu(screen, font, titleFont)
        Config['game']['fps'] = fps
    
        if fps == 30: Config['game']['score'] = 100

        elif fps == 45: Config['game']['score'] = 200

        else: Config['game']['score'] = 300

    elif page == 1: page, highscore = game(screen, font, titleFont, highscore)

    elif page == 3: page = instructions(screen, font, titleFont)

    elif page == 4: page = credits(screen, font, titleFont)

    else: break

pygame.quit()