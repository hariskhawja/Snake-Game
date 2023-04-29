import pygame
import snake
import apple
from functions import textDisplay
from config import Config

def gameReset(snakeBody):
    snakeBody.snakeReset()
    Config['snake']['color'] = Config['colors']['blue']
    return 0, [0, 0]

def game(screen, font, titleFont, highscore):
    fpsClock = pygame.time.Clock()
    snakeBody = snake.Snake()
    appleBody = apple.Apple()
    change = [0, 0]
    score = 0
    Config['snake']['color'] = Config['colors']['blue']

    while True:
        screen.fill([0, 0, 0])

        alive = snakeBody.snakeCollideWall()
        
        snakeBody.snakeDraw(screen)
        appleBody.appleDraw(screen)

        if alive: 
            snakeBody.snakeMove(change[0], change[1])
            textDisplay("Score: " + str(score), font, (50, 50), screen, "l")

        if not alive:
            if score > highscore: highscore = score 
            Config['snake']['color'] = Config['colors']['red']
            pygame.draw.rect(screen, Config['colors']['black'], [200, 150, 400, 300])
            pygame.draw.rect(screen, Config['colors']['white'], [200, 150, 400, 300], width=1)
            textDisplay("Game Over", titleFont, (400, 180), screen, "c")
            textDisplay("Score: " + str(score), titleFont, (210, 220), screen, "l")
            textDisplay("Highscore: " + str(highscore), titleFont, (210, 260), screen, "l")

            restart = pygame.draw.rect(screen, Config['colors']['red'], (260, 340, 100, 50))
            textDisplay("RESTART", font, [310, 365], screen, "c")

            menu = pygame.draw.rect(screen, Config['colors']['blue'], (440, 340, 100, 50))
            textDisplay("MENU", font, [490, 365], screen, "c")

        if snakeBody.body[0] == appleBody.pos:
            snakeBody.snakeExtend()
            appleBody.appleGen()
            score += Config['game']['score']

        for i in range(1, len(snakeBody.body)):
            if snakeBody.body[0] == snakeBody.body[i]: 
                alive = False
                Config['snake']['color'] = Config['colors']['red']

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and change != [0, 1]: change = [0, -1]

                if event.key == pygame.K_DOWN and change != [0, -1]: change = [0, 1]

                if event.key == pygame.K_RIGHT and change != [-1, 0]: change = [1, 0]

                if event.key == pygame.K_LEFT and change != [1, 0]: change = [-1, 0]
            
            if event.type == pygame.MOUSEBUTTONDOWN and not alive:
                if restart.collidepoint(pygame.mouse.get_pos()): score, change = gameReset(snakeBody)

                if menu.collidepoint(pygame.mouse.get_pos()): return 0, highscore

            if event.type == pygame.QUIT: return 9, highscore

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])