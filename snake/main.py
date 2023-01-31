import pygame
import time
import random

from variables import *

pygame.init()
pygame.display.set_caption('Snake by HoweZae')

# INITIALIZATION OF GAME PARAMETERS
CLOCK = pygame.time.Clock()
WINDOW = pygame.display.set_mode((scr_width*2, scr_height*2), pygame.HWSURFACE | pygame.DOUBLEBUF)
SCREEN = pygame.Surface((scr_width, scr_height))
FONT_DEFAULT = pygame.font.SysFont("SF Mono", 9, bold = True)

# GAME FUNCTIONS
def message(type, s):
    color, x, y = msg_types[type]
    msg = FONT_DEFAULT.render(s, True, color)
    SCREEN.blit(msg, [x, y])
    pygame.display.update()

def generateFood():
    x = (random.randint(10, (scr_width-s_size) // 10) * 10)
    y = (random.randint(10, (scr_height-s_size) // 10) * 10)
    return x, y

# GAME MAIN
def main():
    # INITIALIZATION OF IN GAME VARIABLES
    s_posx = scr_width // 2
    s_posy = scr_height // 2
    s_dx, s_dy = 0, 0

    s_score = 0
    s_bodylength = 1
    s_foodx, s_foody = generateFood()

    s_body = []

    while True:
        # quit option
        for event in pygame.event.get():
            # print(event) # for debugging
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):
                    s_dx = -s_speed
                    s_dy = 0
                elif (event.key == pygame.K_d):
                    s_dx = s_speed
                    s_dy = 0
                elif (event.key == pygame.K_w):
                    s_dx = 0
                    s_dy = -s_speed
                elif (event.key == pygame.K_s):
                    s_dx = 0
                    s_dy = s_speed
                elif (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()
        
        # update coordinates of snake, head
        s_posx += s_dx
        s_posy += s_dy
        s_body.append((s_posx,s_posy))

        # when the snake is moving
        if len(s_body) > s_bodylength:
            del s_body[0]

        # lose condition
        if (s_posx >= scr_width or s_posx <= 0) or (s_posy >= scr_height or s_posy <= 0):
            message("lose", "FINAL SCORE: " + str(s_score))
            print(s_posx, s_posy)
            time.sleep(2)
            break

        # INITIALIZATION OF GRAPHICS
        SCREEN.fill(c_bg)
        message("score", "Score: " + str(s_score))

        # draw food
        pygame.draw.rect(SCREEN, c_food, [s_foodx, s_foody, s_foodsize, s_foodsize])

        # draw snake; inefficient, should use classes
        for x,y in s_body:
            pygame.draw.rect(SCREEN, c_snake, [x, y, s_size, s_size])

        # score condition
        if (s_posx in range(s_foodx - s_size//2 - 1, s_foodx)) and (s_posy in range(s_foody - s_size//2 - 1, s_foody)):
            s_foodx, s_foody = generateFood()
            s_score += 1
            s_bodylength += 1

        # GAME UPDATE
        WINDOW.blit(pygame.transform.scale(SCREEN, (scr_width, scr_height)), (0, 0))
        pygame.display.update()
        CLOCK.tick(30)

main()

# ender
pygame.quit()
quit()

## NOTES:
# 