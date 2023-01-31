import pygame

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sheeper\images\crosshairfull.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        pass

class Sheep(pygame.sprite.Sprite):
    state_dict = {
        0: (0,0,20,16),
        1: (20,0,40,16),
        2: (0,0,20,16),
        3: (40,0,60,16)
    }
    source = pygame.image.load("sheeper\images\sheep.png").convert_alpha()
    
    def __init__(self, pos):
        super().__init__()

        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.state_dict[0])
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.state = 0

    def update(self):
        if self.state < 3:
            self.state += 1
        else:
            self.state = 0

        self.image.blit(self.source, (0,0), self.state_dict[self.state])
        self.rect.left += 1

    def updateLeft(self):
        pass

    def scram(self):
        pass

    def eatGrass(self):
        pass