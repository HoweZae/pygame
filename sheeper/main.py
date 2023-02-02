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
    grass_bg = pygame.Surface((320,240))
    for x in range(0, 324, 81):
        for y in range(0, 243, 81):
            grass_bg.blit(grass, (x, y))

    # SHEEP INITIALIZATION
    sheep_group = pygame.sprite.Group()
    sheep_count = 8
    for i in range(sheep_count):
        sheep_group.add(Sheep((random.randrange(1,16-1)*20, random.randrange(1,15-1)*16)))

    # CROSSHAIR INITIALIZATION
    xhair = Crosshair()
    xhair_group = pygame.sprite.Group(xhair)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # RENDER BACKGROUND
        screen.blit(grass_bg, (0,0))
        
        # RENDER SHEEPS
        for i in range(1,sheep_count):
            if i % 2 == 0:
                sheep_group.sprites()[i].walkRight()
            else:
                sheep_group.sprites()[i].walkLeft()

        # RENDER EVERYTHING ELSE
        sheep_group.draw(screen)

        WINDOW.blit(pygame.transform.scale_by(screen, 2), (0, 0))

        xhair_group.update()
        xhair_group.draw(WINDOW)

        pygame.display.update()
        CLOCK.tick(60)

main()