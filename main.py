import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = pygame.display.set_caption("Dragonwind")
clock = pygame.time.Clock()

moving_left = False
moving_right = False
BG_COLOR = (0, 124, 124)

def set_background():
    screen.fill(BG_COLOR)

class Dungeoneer(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/player/idle.png').convert()
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = img.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, self.rect)

player = Dungeoneer(100, 100, 3, 5)

FPS = 60
running = True
while running:
    set_background()
    player.draw()
    player.move(moving_left, moving_right)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()