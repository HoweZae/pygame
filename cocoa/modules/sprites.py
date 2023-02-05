import pygame

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, imgpath, w, h, frameli):
        super().__init__()
        self.sheet = pygame.image.load(imgpath).convert_alpha()
        self.frameli = frameli
        self.size = (w,h)
        self.tick = 0
        self.frame = 0

    def get_image(self, frame, lookingLeft):
        image = pygame.Surface(self.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), self.frameli[frame])

        if lookingLeft:
            return pygame.transform.flip(image, True, False)
        return image

class Player(Spritesheet):
    def __init__(self, x, y):
        fli = (
            (0,0,25,27),
            (25,0,50,27),
            (50,0,75,27),
            (75,0,100,27),
            (50,0,75,27),
            (25,0,50,27),
            (0,0,25,27),
            (100,0,125,27),
            (125,0,150,27),
            (100,0,125,27)
        )
        super().__init__("cocoa\images\office frog.png", 25, 27, fli)
        self.image = super().get_image(0, False)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 120)
        self.x = x
        self.y = y

        self.momentum = 0

        self.moving = False
        self.lookingLeft = False

    def update(self):
        if self.moving:
            self.momentum += 1
            self.run(self.lookingLeft)

        else:
            self.momentum -= 1

    def idle(self):
        self.image = super().get_image(0, self.lookingLeft)
        self.moving = False
        self.tick = 0
        self.frame = 0

    def run(self, lookingLeft):
        self.tick += 1
        frame = (self.tick // 6) % 10 # len frameli
        self.image = super().get_image(frame, lookingLeft)
        if frame != self.frame:
            self.frame = frame

    def walk(self):
        pass