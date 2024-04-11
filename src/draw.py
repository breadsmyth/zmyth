import pygame

def draw_all(screen):
    'Draws all panels to the screen'
    screen_x, screen_y = screen.get_size()

    panel_width = screen_x // 5
    margin = screen_y // 60
    panel_height = screen_y - (margin * 2)


    # Inventory panel
    inv_panel = pygame.Surface((panel_width - margin, panel_height))
    inv_panel.fill((0, 0, 0))
    screen.blit(inv_panel, (screen_x - panel_width, margin))


    # Recipes panel
    rec_panel = pygame.Surface((panel_width - margin, panel_height))
    rec_panel.fill((0, 0, 0))
    screen.blit(rec_panel, (margin, margin))


    # Game window
    game_panel = pygame.Surface((panel_width * 3 - margin * 2, panel_height))
    game_panel.fill((0, 0, 0))
    screen.blit(game_panel, (panel_width + margin, margin))
