import pygame
from ship import Ship
from settings import Settings
from game_functions import *
from pygame.sprite import Group
from alien import Alien

def run_game():
    # Initialize the game and create screen obj.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion -- Rubing")
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    #f = open("rect_ship.txt", "w")
    # Make a group to store bullets in.
    bullets = Group()
    # Start the main loop for the game
    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        #bullets.update_bullet()#'Group' object has no attribute 'update_bullet'
        update_bullets(bullets)
        #f.write("%d\t%d\t%d\t%d\n" % (ship.ship_rect.centerx, ship.screen_rect.centerx, ship.screen_rect.top, ship.screen_rect.bottom))
        update_screen(ai_settings, screen, ship, alien, bullets)
run_game()
#f.close()
