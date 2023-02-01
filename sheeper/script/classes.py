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
    frames = {
        0: (0,0,20,16),
        1: (20,0,40,16),
        2: (0,0,20,16),
        3: (40,0,80,16)
    }
    source = pygame.image.load("sheeper\images\sheepwalk.png").convert_alpha()
    
    def __init__(self, pos):
        super().__init__()
        self.tick = 0
        self.frame = 0

        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.frames[0])
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def eatGrass(self):
        pass

    def walkRight(self):
        self.tick += 1

        frame = (self.tick // 6) % 4
        
        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.frames[frame])
        self.image = image

        if (frame != self.frame):
            self.rect.left += 1
            self.frame = frame

    def walkLeft(self):
        self.tick += 1

        frame = (self.tick // 6) % 4
        
        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.frames[frame])
        self.image = pygame.transform.flip(image, True, False)

        if (frame != self.frame):
            self.rect.left -= 1
            self.frame = frame