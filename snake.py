from config import Config
import pygame

class Snake:
    def __init__(self):
        self.body = [[400, 300]]
        self.extension = []
        self.length = 1

    def snakeDraw(self, screen):
        for i in self.body:
            pygame.draw.rect(screen, Config['snake']['color'], (i[0], i[1], Config['snake']['width'], Config['snake']['height']))
    
    def snakeMove(self, x, y):
        if not (x == 0 and y == 0):
            newHead = [self.body[0][0] + x * Config['snake']['speed'], self.body[0][1] + y * Config['snake']['speed']]
            self.body.insert(0, newHead)
            self.extension = self.body.pop()
        
    def snakeExtend(self):
        self.body.append(self.extension)
        self.length += 1

    def snakeCollideWall(self):
        if self.body[0][0] < 0 or self.body[0][0] > 800 or self.body[0][1] < 0 or self.body[0][1] > 600: return False

        else: return True
    
    def snakeReset(self):
        self.body = [[400, 300]]
        self.extension = []
        self.length = 1