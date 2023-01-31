import pygame

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.Surface((19,19))
        image.blit(pygame.image.load("crosshair shooter\crosshair.png"), (0,0))
        image.set_colorkey((255, 0, 255))

        self.image = pygame.transform.scale(image, (38, 38))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        pass

class Sheep(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        image = pygame.Surface((32,32))
        image.blit((pygame.image.load("crosshair shooter\sheep.png")), pos)
        image.set_colorkey((255, 0, 255))

        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = pos