import pygame
import snake
import apple
from config import Config

textX = lambda x : x + 20
textY = lambda y : y + 15

def textDisplay(text, font, coordinates, screen, pos):
    text = font.render(text, True, [255, 255, 255])

    if pos == "c":  textRect = text.get_rect(center=coordinates)

    if pos == "l":  textRect= text.get_rect(topleft=coordinates)

    screen.blit(text, textRect)

def gameReset(snakeBody):
    snakeBody.snakeReset()
    Config['snake']['color'] = Config['colors']['blue']
    return 0, [0, 0]

def menu(screen, font, titleFont):
    quitVar = True
    fpsClock = pygame.time.Clock()

    while quitVar:
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

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy.collidepoint(pygame.mouse.get_pos()):
                    return 1, 30
                
                if mid.collidepoint(pygame.mouse.get_pos()):
                    return 1, 45
                
                if hard.collidepoint(pygame.mouse.get_pos()):
                    return 1, 60
                
                if credits.collidepoint(pygame.mouse.get_pos()):
                    return 4, 30

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])

def game(screen, font):
    quitVar = True
    fpsClock = pygame.time.Clock()
    snakeBody = snake.Snake()
    appleBody = apple.Apple()
    change = [0, 0]
    score = 0
    alive = True
    Config['snake']['color'] = Config['colors']['blue']

    while quitVar:
        screen.fill([0, 0, 0])

        alive = snakeBody.snakeCollideWall()
        
        snakeBody.snakeDraw(screen)
        appleBody.appleDraw(screen)

        if alive: 
            snakeBody.snakeMove(change[0], change[1])
            textDisplay("Score: " + str(score), font, (50, 50), screen, "l")

        if not alive: 
            Config['snake']['color'] = Config['colors']['red']
            textDisplay("Score: " + str(score), font, (400, 300), screen, "l")

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

                if event.key == pygame.K_r: score, change = gameReset(snakeBody)

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])

def credits(screen, font, titleFont):
    quitVar = True
    fpsClock = pygame.time.Clock()

    while quitVar:
        screen.fill([0, 0, 0])
        textDisplay("Credits", titleFont, (50, 100), screen, "l")
        textDisplay("Designer: Haris Khawja", font, (50, 150), screen, "l")
        textDisplay("Supervisors: Coach Asad, Coach Saeesh", font, (50, 200), screen, "l")
        textDisplay("Company: Zebra Robotics", font, (50, 250), screen, "l")
        textDisplay("Language: Python 3, Pygame", font, (50, 300), screen, "l")
        textDisplay("Completion Date: ???", font, (50, 350), screen, "l")

        menu = pygame.draw.rect(screen, Config['colors']['blue'], (350, 500, 100, 30))
        textDisplay("MENU", font, [400, textY(500)], screen, "c")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.collidepoint(pygame.mouse.get_pos()): return 0

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        fpsClock.tick(Config['game']['fps'])

