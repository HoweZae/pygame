# demonstration of collisions
import pygame, sys

# bouncing rectangles function
def bouncing_rect():
    # global declaration
    global rect1_vx, rect1_vy
    global rect2_vy

    # moving white
    rect1.x += rect1_vx
    rect1.y += rect1_vy

    # moving blue
    rect2.y += rect2_vy

    # when colliding with border of screen:
    if rect1.right >= 320 or rect1.left <= 0:
        rect1_vx *= -1
    if rect1.bottom >= 240 or rect1.top <= 0:
        rect1_vy *= -1

    if rect2.bottom >= 240 or rect2.top <= 0:
        rect2_vy *= -1

    # when colliding with each other:
    # to accomodate skipped frames
    collision_tol = 5

    if rect1.colliderect(rect2):
        # when rect2 hits bottom of rect1
        if abs(rect2.top - rect1.bottom) < collision_tol and rect1_vy > 0:
            rect1_vy *= -1

        # when rect2 hits top of rect1
        elif abs(rect2.bottom - rect1.top) < collision_tol and rect1_vy < 0:
            rect1_vy *= -1

        # when rect2 hits left of rect1
        if abs(rect2.left - rect1.right) < collision_tol and rect1_vx > 0:
            rect1_vx *= -1

        # when rect2 hits right of rect1
        if abs(rect2.right - rect1.left) < collision_tol and rect1_vx < 0:
            rect1_vx *= -1

    pygame.draw.ellipse(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (0,255,255), rect2)

pygame.init()
WINDOW = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
CLOCK = pygame.time.Clock()

screen = pygame.surface.Surface((320, 240))

# white
rect1 = pygame.Rect(160-10, 80-10, 20, 20)
rect1_vx = 2
rect1_vy = 2

# blue
rect2 = pygame.Rect(160-50, 120-15, 100, 30)
rect2_vy = 1

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))
        bouncing_rect()

        WINDOW.blit(pygame.transform.scale_by(screen, 2), (0, 0))
        pygame.display.update()
        CLOCK.tick(100)
        # ticks at 100 fps; feel free to scale down if shit rig na emz

main()