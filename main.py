import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Dragonwind")
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    clock.tick(FPS)

pygame.quit()