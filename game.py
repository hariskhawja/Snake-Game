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

    while quitVar:
        screen.fill([0, 0, 0])
        
        snakeBody.snakeDraw(screen)
        snakeBody.move(change[0], change[1])

        appleBody.appleDraw(screen)

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