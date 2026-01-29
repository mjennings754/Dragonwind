import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Dragonwind")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()