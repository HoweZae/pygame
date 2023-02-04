import pygame
import sys

from scripts.sprites import *
from scripts.variables import *

pygame.init()

WINDOW = pygame.display.set_mode((windowW, windowH), pygame.HWSURFACE | pygame.DOUBLEBUF)
CLOCK = pygame.time.Clock()

screen = pygame.surface.Surface((320, 240))

# SPRITES INITIALIZATION
player = Player((160, 120))
player_group = pygame.sprite.Group(player)

def main():
    vel_x = 0
    vel_y = 0

    # MAIN GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w):
                    vel_y += 1
                    player.moving = True
                if (event.key == pygame.K_s):
                    vel_y -= 1
                    player.moving = True
                if (event.key == pygame.K_a):
                    vel_x -= 1
                    player.moving = True
                    player.lookingLeft = True
                if (event.key == pygame.K_d):
                    vel_x += 1
                    player.moving = True
                    player.lookingLeft = False
                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()

            elif event.type == pygame.KEYUP:
                player.idle()
                vel_x = 0
                vel_y = 0

        screen.fill(c_gray)

        player_group.update()
        player_group.draw(screen)

        #rendering
        WINDOW.blit(pygame.transform.scale(screen, (windowW, windowH)), (0, 0))
        pygame.display.update()
        CLOCK.tick(60)

main()