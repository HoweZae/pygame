import pygame
import sys

pygame.init()
SCREEN = pygame.display.set_mode((640, 480))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((0,255,255))
        pygame.display.flip()

main()