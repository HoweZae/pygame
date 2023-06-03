import pygame

class Level:
    def __init__(self, screen):
        self.screen = screen

        # initialization of visible and obstacle sprites
        self.visibles = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()



    def run(self):
        pass