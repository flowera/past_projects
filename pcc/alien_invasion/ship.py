import pygame
from settings import Settings

class Ship():
    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.image.get_rect()
        print(self.ship_rect)
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom
        # Store a decimal value for ship's center
        self.center = float(self.ship_rect.centerx)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            #self.ship_rect.centerx += 1
            self.center += self.settings.ship_speed_factor

        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
        # Update rect obj from self.center.
        #print(self.center)

        self.ship_rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.ship_rect)
