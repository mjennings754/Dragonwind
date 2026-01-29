import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Dragonwind")
clock = pygame.time.Clock()

class Dungeoneer(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/player/idle.png').convert()
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = img.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

player = Dungeoneer(100, 100, 3)

FPS = 60
running = True
while running:
    player.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()