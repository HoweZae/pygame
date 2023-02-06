import pygame, sys

from config import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Zelda Game')

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((SCREEN_W*2, SCREEN_H*2), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen = pygame.surface.Surface((SCREEN_W, SCREEN_H))

        self.level = Level(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        pass
                    if event.key == pygame.K_s:
                        pass
                    if event.key == pygame.K_a:
                        pass
                    if event.key == pygame.K_d:
                        pass

            self.screen.fill('white')
            self.level.run()

            self.window.blit(pygame.transform.scale_by(self.screen, 2), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()