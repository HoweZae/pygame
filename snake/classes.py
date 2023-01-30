import pygame

# SNAKE CLASS (to be continued)
class Snake:
    def __init__(self, size, body, x, y):
        self.size = size
        self.body = body

        self.head = pygame.Surface((size, size))
        self.head.center = (x, y)

    def render(self):
        for e in self.body:
            pass

    def lengthen(self):
        self.size += 1
        pass