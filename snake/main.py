import pygame
import time
import random

# INITIALIZATION OF GLOBAL CONSTANTS
# colors:
c_white = (255,255,255)
c_richblack = (0, 16, 17)
c_babyblue = (108, 207, 246)
c_lightgreen = (145, 245, 173)
c_lavender = (108, 207, 246)

c_snake = c_lightgreen
c_food = c_babyblue
c_bg = c_richblack
c_contrast = (abs(255-c_bg[0]), abs(255-c_bg[1]), abs(255-c_bg[2]))
c_text = c_white

# screen size:
scr_width = 640
scr_height = 480

# snake/game:
s_size = 20
s_speed = 10
s_foodsize = 10

# message
# UNOPTIMIZED; find a way to do this that does not make use of strings as keys
msg_types = {
    "lose": (c_text, scr_width//2, scr_height//2),
    "score": (c_text, 0, 0),
    "update": (c_text, 540, 0)
}

pygame.init()
pygame.display.set_caption('Snake by HoweZae')

# INITIALIZATION OF GAME PARAMETERS
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((scr_width, scr_height))
FONT_DEFAULT = pygame.font.SysFont("SF Mono", 18, bold=True)

# GAME FUNCTIONS
def message(type, s):
    color, x, y = msg_types[type]
    msg = FONT_DEFAULT.render(s, True, color)
    SCREEN.blit(msg, [x, y])
    pygame.display.update()

# GAME MAIN
def main():
    # INITIALIZATION OF IN GAME VARIABLES
    s_posx = scr_width // 2
    s_posy = scr_height // 2
    s_dx, s_dy = 0, 0

    s_score = 0
    s_bodylength = 1
    s_foodx = (random.randint(0, (scr_width-s_size) // 20) * 20) + 5
    s_foody = (random.randint(0, (scr_height-s_size) // 20) * 20) + 5

    s_body = []

    print(s_foodx, s_foody)

    while True:
        # quit option
        for event in pygame.event.get():
            # print(event) # for debugging
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):
                    s_dx, s_dy = -s_speed, 0
                elif (event.key == pygame.K_d):
                    s_dx, s_dy = s_speed, 0
                elif (event.key == pygame.K_w):
                    s_dx, s_dy = 0, -s_speed
                elif (event.key == pygame.K_s):
                    s_dx, s_dy = 0, s_speed
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
        if (s_posx >= scr_width - s_size//2 or s_posx <= 0) or (s_posy >= scr_height - s_size//2 or s_posy <= 0) or ((s_posx,s_posy) in s_body[:-1:]):
            message("lose", "FINAL SCORE: " + str(s_score))
            time.sleep(2)
            break

        # INITIALIZATION OF GRAPHICS
        SCREEN.fill(c_bg)
        message("score", "Score: " + str(s_score))
        pygame.draw.rect(SCREEN, c_food, [s_foodx, s_foody, s_foodsize, s_foodsize])

        for x,y in s_body:
            pygame.draw.rect(SCREEN, c_snake, [x, y, s_size, s_size])

        # score condition
        if (s_posx in range(s_foodx - s_size//2 - 1, s_foodx)) and (s_posy in range(s_foody - s_size//2 - 1, s_foody)):
            s_score += 1
            s_bodylength += 1

        # GAME UPDATE
        pygame.display.update()
        CLOCK.tick(30)

main()

# ender
pygame.quit()
quit()

## NOTES:
# 