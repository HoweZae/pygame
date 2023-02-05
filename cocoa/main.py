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
    press_w = False
    press_s = False
    press_a = False
    press_d = False

    # MAIN GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w):
                    press_w = True
                    vel_y += 1
                    player.moving = True
                if (event.key == pygame.K_s):
                    press_s = True
                    vel_y -= 1
                    player.moving = True
                if (event.key == pygame.K_a):
                    press_a = True
                    vel_x -= 1
                    player.moving = True
                    player.lookingLeft = True
                if (event.key == pygame.K_d):
                    press_d = True
                    vel_x += 1
                    player.moving = True
                    player.lookingLeft = False

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_w):
                    press_w = False
                if (event.key == pygame.K_s):
                    press_s = False
                if (event.key == pygame.K_a):
                    press_a = False
                if (event.key == pygame.K_d):
                    press_d = False

        screen.fill(c_gray)

        if not (press_w or press_s or press_a or press_d):
            player.idle()

        player_group.update()
        player_group.draw(screen)

        #rendering
        WINDOW.blit(pygame.transform.scale(screen, (windowW, windowH)), (0, 0))
        pygame.display.update()
        CLOCK.tick(60)

main()