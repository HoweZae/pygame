import pygame
import sys

from scripts.sprites import *
from scripts.variables import *

pygame.init()

windowW = 640
windowH = 480
WINDOW = pygame.display.set_mode((windowW, windowH), pygame.HWSURFACE | pygame.DOUBLEBUF)
CLOCK = pygame.time.Clock()

screen = pygame.surface.Surface((320, 240))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('white')
        pygame.draw.rect(screen, (108, 207, 246), [20, 20, 20, 20])

        #rendering
        WINDOW.blit(pygame.transform.scale(screen, (windowW, windowH)), (0, 0))
        pygame.display.update()
        CLOCK.tick(60)

main()