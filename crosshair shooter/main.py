import pygame, sys

from pygame.transform import scale

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = scale(pygame.image.load("crosshair shooter\crosshair.png"), (640, 480))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        pass

pygame.init()
CLOCK = pygame.time.Clock()

# GAME SCREEN
WINDOW = pygame.display.set_mode((640, 480))
screen = pygame.Surface((320, 240))

# BACKGROUND
grass = pygame.image.load("crosshair shooter\grass.png")

# CROSSHAIR
xhair = Crosshair()
xhair_group = pygame.sprite.Group()
xhair_group.add(xhair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for x in range(0, 320, 32):
        for y in range(0, 240, 32):
            screen.blit(grass, (x, y))

    WINDOW.blit(scale(screen, (640, 480)), (0, 0))

    xhair_group.draw(WINDOW)
    xhair_group.update()

    pygame.display.update()
    CLOCK.tick(60)