import constants
import draw
from file_handlers import settings

import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.display.init()

settings_obj = settings.load()
resolution = tuple(settings_obj['resolution'])

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption(constants.TITLE)


running = True
while running:
    screen.fill((20, 20, 20))

    draw.draw_all(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
