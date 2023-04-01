import pygame
import snake
import apple
from config import Config

def game(screen):
    quitVar = True
    fpsClock = pygame.time.Clock()
    snakeBody = snake.Snake()
    appleBody = apple.Apple()
    change = [0, 0]
    alive = True

    Config['snake']['color'] == Config['colors']['blue']

    while quitVar:
        screen.fill([0, 0, 0])
        
        snakeBody.snakeDraw(screen)
        appleBody.appleDraw(screen)

        if alive: snakeBody.snakeMove(change[0], change[1])

        if snakeBody.body[0] == appleBody.pos:
            snakeBody.snakeExtend()
            appleBody.appleGen()

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

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])