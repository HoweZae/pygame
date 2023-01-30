import pygame
# from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.HWSURFACE| pygame.DOUBLEBUF| pygame.RESIZABLE)
    pic = pygame.surface.Surface((320, 240))
    pic.fill('white')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()

        pygame.draw.rect(pic, (108, 207, 246), [20, 20, 20, 20])

        screen.blit(pygame.transform.scale(pic, (640, 480)), (0,0))
        # screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()
    
main()   