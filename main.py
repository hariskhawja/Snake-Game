import pygame
from config import Config
import game

pygame.init()
pygame.display.set_caption("Snake Game")

screen = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))

font = pygame.font.SysFont(Config['game']['font'], Config['game']['fontSize'])

game.game(screen)

pygame.quit()