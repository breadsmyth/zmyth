import pygame

import constants
import draw
import game
from file_handlers import settings


pygame.init()
clock = pygame.time.Clock()
pygame.display.init()
game.init()


settings_obj = settings.load()
resolution = tuple(settings_obj['resolution'])
is_fullscreen = settings_obj['fullscreen']

display_flags = pygame.SCALED
if is_fullscreen:
    display_flags |= pygame.FULLSCREEN

screen = pygame.display.set_mode(resolution, display_flags)
pygame.display.set_caption(constants.TITLE)


running = True
while running:
    draw.draw_current_context(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
