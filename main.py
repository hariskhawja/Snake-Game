import pygame
import game
from config import Config

pygame.init()
pygame.display.set_caption("Snake Game")

page = 0

screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

font = pygame.font.SysFont(Config['game']['font'], Config['game']['fontSize'])

if page == 0: page = game.menu(screen, font)

if page == 1: game.game(screen, font)

pygame.quit()