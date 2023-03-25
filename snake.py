from config import Config
import pygame

class Snake:
    def __init__(self):
        self.body = [[400, 300], [410, 300]]

    def snakeDraw(self, screen):
        for i in self.body:
            pygame.draw.rect(screen, Config['colors']['blue'], (i[0], i[1], Config['snake']['width'], Config['snake']['height']))
    
    def move(self, x, y):
        if not (x == 0 and y == 0):
            previous = self.body[0]
            print("PREVIOUS0: ", previous)
            
            self.body[0][0] += x * Config['snake']['speed']
            self.body[0][1] += y * Config['snake']['speed']

            print("PREVIOUS/: ", previous)

            current = []

            print("PREVIOUS: ", previous)

            for i in range(1, len(self.body)):
                print("BODY: ", self.body[i])
                current = self.body[i]
                print("CURRENT: ", current)
                print("PREVIOUS2: ", previous)
                self.body[i] = previous
                print("BODYNEW: ", self.body[i])
                previous = current