import pygame
from rocket import Rocket
from settings import Settings
from game_functions import *

def run_game():
    # Initialize the game and create screen obj.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket War -- Rubing")
    rocket = Rocket(ai_settings, screen)

    # Start the main loop for the game
    while True:
        check_events(rocket)
        rocket.update()
        #f.write("%d\t%d\t%d\t%d\n" % (ship.ship_rect.centerx, ship.screen_rect.centerx, ship.screen_rect.top, ship.screen_rect.bottom))
        update_screen(ai_settings, screen, rocket)
run_game()
