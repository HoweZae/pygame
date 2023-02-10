import pygame
from config import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # # add when we have a sprite na
        # self.image = pygame.image.load("zelda\images\smth.png").convert_alpha()
        self.image = pygame.Rect(0,0,32,32).fill((0,0,0))
        self.rect = self.image.get_rect(topleft = pos)
        self.rect.center = (SCREEN_W // 2, SCREEN_H // 2)
