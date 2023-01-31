import pygame, sys
import random

from script.classes import *

pygame.init()
CLOCK = pygame.time.Clock()

# GAME SCREEN
WINDOW = pygame.display.set_mode((640, 480))
screen = pygame.Surface((320, 240))
pygame.mouse.set_visible(False)

def main():
    # BACKGROUND
    grass = pygame.image.load("sheeper\images\grass.png")
    for x in range(0, 320, 32):
        for y in range(0, 240, 32):
            screen.blit(grass, (x, y))

    # SHEEP INITIALIZATION
    sheep_group = pygame.sprite.Group()
    memo = set([])
    iter, count = 0, 8
    while iter < count:
        pos = (random.randint(32, 320 - 32), random.randint(32, 240 - 32))
        if pos not in memo:
            sheep_group.add(Sheep(pos))
            memo.add(pos)
            iter += 1

    # CROSSHAIR INITIALIZATION
    xhair = Crosshair()
    xhair_group = pygame.sprite.Group(xhair)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        sheep_group.draw(screen)

        WINDOW.blit(pygame.transform.scale(screen, (640, 480)), (0, 0))

        xhair_group.draw(WINDOW)
        xhair_group.update()

        pygame.display.update()
        CLOCK.tick(60)

main()