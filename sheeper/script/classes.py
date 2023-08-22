import pygame

# SUPERCLASS
class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, imgpath, w, h, frame_dict = None):
        super().__init__()
        self.sheet = pygame.image.load(imgpath).convert_alpha()
        self.frame_dict = frame_dict
        self.size = (w,h)
        self.tick = 0
        self.frame = 0

    def get_image(self, frame):
        image = pygame.Surface(self.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), self.frame_dict[frame])
        return image

# SPRITESHEET SUBCLASSES
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sheeper\images\crosshairfull.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        pass

class Sheep(Spritesheet):
    def __init__(self, pos):
        frame_dict = {
            0: (0, 0, 20, 16),
            1: (20, 0, 40, 16),
            2: (0, 0, 20, 16),
            3: (40, 0, 60, 16)
        }
        super().__init__("sheeper\images\sheepwalk.png", 20, 16, frame_dict)
        self.image = super().get_image(frame = 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def eatGrass(self):
        pass

    def walkRight(self):
        self.tick += 1
        frame = (self.tick // 6) % 4
        self.image = super().get_image(frame)
        if (frame != self.frame):
            self.rect.left += 1
            self.frame = frame

    def walkLeft(self):
        self.tick += 1
        frame = (self.tick // 6) % 4
        self.image = pygame.transform.flip(super().get_image(frame), True, False)
        if (frame != self.frame):
            self.rect.left -= 1
            self.frame = frame