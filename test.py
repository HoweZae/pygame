import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

testsurface = pygame.Surface((100,100))
testsurface.fill((140,48,116))
testX = 200
testY = 250

while True:

    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fill with color
    screen.fill((152,218,242))

    # some random code where the box shakes
    if testX % 2 == 0:
        testX += 3
    else:
        testX -= 3
    if testY % 2 == 0:
        testY += 3
    else:
        testY -= 3

    # block image transfer (with position @ top left)
    screen.blit(testsurface,(testX,testY))

    pygame.display.update()
    clock.tick(30)