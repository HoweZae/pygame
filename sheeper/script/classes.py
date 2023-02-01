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
        0: (0,0,20,16),     # 1
        1: (20,0,40,16),    # 2
        2: (40,0,60,16),    # 3
        3: (20,0,40,16),
        4: (0,0,20,16),
        5: (60,0,80,16),    # 4
        6: (80,0,100,16),   # 5
        7: (60,0,80,16)
    }
    source = pygame.image.load("sheeper\images\sheep.png").convert_alpha()
    
    def __init__(self, pos):
        super().__init__()
        self.state = 0

        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.state_dict[int(self.state)])
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        self.state += 0.2
        if self.state > 7:
            self.state = 0
        
        state = int(self.state)

        image = pygame.Surface((20,16), pygame.SRCALPHA)
        image.blit(self.source, (0,0), self.state_dict[state])
        self.image = image
        
        # if state % 2 == 0:
        self.rect.left += 1

    def changeDir(self):
        pass
    def scram(self):
        pass
    def eatGrass(self):
        pass