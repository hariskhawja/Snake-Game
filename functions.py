def textDisplay(text, font, coordinates, screen, pos):
    text = font.render(text, True, [255, 255, 255])

    if pos == "c":  textRect = text.get_rect(center=coordinates)

    if pos == "l":  textRect= text.get_rect(topleft=coordinates)

    screen.blit(text, textRect)

textY = lambda y : y + 15