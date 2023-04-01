from config import Config
import pygame
import random

class Apple:
    def __init__(self):
        self.pos = [400, 330]
        active = True

    def appleDraw(self, screen):
        pygame.draw.rect(screen, Config['colors']['appleRed'], (self.pos[0], self.pos[1], Config['apple']['width'], Config['apple']['height']))

    def appleGen(self):
        self.pos = [random.randrange(0, 80, 1) * 10, random.randrange(0, 60, 1) * 10]