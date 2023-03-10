import pygame

pygame.init()

font = pygame.font.Font(None, 30)

def debug(info, x=10, y=10):
    window = pygame.display.get_surface()
    debug_surface = font.render(str(info), True, 'white')
    debug_rect = debug_surface.get_rect(topleft = (x,y))
    
    pygame.draw.rect(window,'Black',debug_rect)
    window.blit(debug_surface, debug_rect)