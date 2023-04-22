import pygame
import game
from config import Config

pygame.init()
pygame.display.set_caption("Snake Game")

page = 0

screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

font = pygame.font.SysFont(Config['game']['font'], Config['game']['fontSize'])
titleFont = pygame.font.SysFont(Config['game']['font'], Config['game']['titleSize'])

if page == 0: 
    page, fps = game.menu(screen, font, titleFont)
    Config['game']['fps'] = fps
    
    if fps == 30: Config['game']['score'] = 100

    if fps == 45: Config['game']['score'] = 200

    if fps == 60: Config['game']['score'] = 300

if page == 1: page = game.game(screen, font, titleFont)

if page == 3: page = game.instructions(screen, font, titleFont)

if page == 4: page = game.credits(screen, font, titleFont)

pygame.quit()