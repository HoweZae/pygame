import pygame, sys
import random

pygame.init()
CLOCK = pygame.time.Clock()

# GAME SCREEN
WINDOW = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
screen = pygame.Surface((320, 240))
pygame.mouse.set_visible(False)

from script.classes import *

def main():
    # BACKGROUND INITIALIZATION
    grass = pygame.image.load("sheeper\images\grass.png")

    # SHEEP INITIALIZATION
    sheep_group = pygame.sprite.Group()
    for i in range(8):
        sheep_group.add(Sheep((random.randrange(1,16-1)*20, random.randrange(1,15-1)*16)))

    # CROSSHAIR INITIALIZATION
    xhair = Crosshair()
    xhair_group = pygame.sprite.Group(xhair)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # EVERYTHING DISPLAY RELATED
        for x in range(0, 324, 81):
            for y in range(0, 243, 81):
                screen.blit(grass, (x, y))

        sheep_group.update()
        sheep_group.draw(screen)

        WINDOW.blit(pygame.transform.scale_by(screen, 2), (0, 0))

        xhair_group.update()
        xhair_group.draw(WINDOW)

        pygame.display.update()
        CLOCK.tick(60)

main()