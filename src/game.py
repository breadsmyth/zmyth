'Manages global state for the game'

CONTEXT_MAIN_MENU = 0
CONTEXT_GAMEPLAY = 1

def init():
    global CONTEXT
    CONTEXT = CONTEXT_MAIN_MENU