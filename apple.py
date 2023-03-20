from config import Config
import pygame
import random

class Apple:
    def __init__(self):
        self.pos = [200, 200]

    def appleDraw(self, screen):
        pygame.draw.rect(screen, Config['colors']['appleRed'], (self.pos[0], self.pos[1], Config['apple']['width'], Config['apple']['height']))

    def randomGen(self):
        pass