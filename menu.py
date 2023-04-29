import pygame
from functions import textDisplay, textY
from config import Config

def menu(screen, font, titleFont):
    fpsClock = pygame.time.Clock()

    while True:
        screen.fill([0, 0, 0])

        textDisplay("Welcome to Snake Game", titleFont, [400, 200], screen, "c")

        easy = pygame.draw.rect(screen, Config['colors']['green'], (350, 280, 100, 30))
        textDisplay("EASY", font, [400, textY(280)], screen, "c")

        mid = pygame.draw.rect(screen, Config['colors']['yellow'], (350, 330, 100, 30))
        textDisplay("MID", font, [400, textY(330)], screen, "c")

        hard = pygame.draw.rect(screen, Config['colors']['red'], (350, 380, 100, 30))
        textDisplay("HARD", font, [400, textY(380)], screen, "c")

        credits = pygame.draw.rect(screen, Config['colors']['blue'], (350, 430, 100, 30))
        textDisplay("CREDITS", font, [400, textY(430)], screen, "c")

        instructions = pygame.draw.rect(screen, Config['colors']['teal'], (350, 480, 100, 30))
        textDisplay("HELP", font, [400, textY(480)], screen, "c")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy.collidepoint(pygame.mouse.get_pos()): return 1, 30
                
                if mid.collidepoint(pygame.mouse.get_pos()): return 1, 45
                
                if hard.collidepoint(pygame.mouse.get_pos()): return 1, 60

                if instructions.collidepoint(pygame.mouse.get_pos()): return 3, 30
                
                if credits.collidepoint(pygame.mouse.get_pos()): return 4, 30

            if event.type == pygame.QUIT: return 9, 30

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])