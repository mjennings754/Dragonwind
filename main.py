import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Dragonwind")
clock = pygame.time.Clock()
x = 200
y = 200
scale = 3
player = pygame.image.load('images/player/idle.png').convert()
player = pygame.transform.scale(player, (player.get_width() * scale, player.get_height() * scale))
rect = player.get_rect()
rect.center = (x, y)

FPS = 60
running = True
while running:
    screen.blit(player, rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()