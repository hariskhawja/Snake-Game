from config import Config
import pygame

class Snake:
    def __init__(self):
        self.body = [[400, 300]]
        self.length = 1

    def snakeDraw(self, screen):
        pygame.draw.rect(screen, Config['colors']['blue'], (self.body[0][0], self.body[0][1], Config['snake']['width'], Config['snake']['height']))
    
    def move(self, x, y):
        self.body[0][0] += x
        self.body[0][1] += y