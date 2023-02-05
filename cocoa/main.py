import pygame
import sys

# # currently dysfunctional; will fix in a while
# from pytmx.util_pygame import load_pygame
# tmx_data = load_pygame("cocoa\config\office.tmx")

from modules.sprites import *
from modules.variables import *

pygame.init()

WINDOW = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
CLOCK = pygame.time.Clock()

screen = pygame.surface.Surface((320, 240))
screen.fill(c_black)
bg = pygame.image.load("cocoa\images\office.png")

# SPRITES INITIALIZATION
player = Player(275, 800)
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
                    vel_y -= 1
                    player.moving = True
                if (event.key == pygame.K_s):
                    press_s = True
                    vel_y += 1
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

        player.x += vel_x
        player.y += vel_y
        print(vel_x, vel_y)

        screen.blit(bg, (0,0), (player.x-160, player.y-120, 320, 240))

        if not (press_w or press_s or press_a or press_d):
            player.idle()
            vel_x = 0
            vel_y = 0

        player_group.update()
        player_group.draw(screen)

        #rendering
        WINDOW.blit(pygame.transform.scale_by(screen, 2), (0, 0))
        pygame.display.update()
        CLOCK.tick(60)

main()