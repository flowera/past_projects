import pygame
from settings import Settings

class Doodler():
    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/Doodler.png')
        self.doodler_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.doodler_rect.left = self.screen_rect.left
        self.doodler_rect.bottom = self.screen_rect.bottom
        # Store a decimal value for ship's center
        self.x = float(self.doodler_rect.centerx)
        self.y = float(self.doodler_rect.centery)
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.doodler_rect.right < self.screen_rect.right:
            #self.ship_rect.centerx += 1
            self.x += self.settings.doodler_speed_factor

        if self.moving_left and self.doodler_rect.left > self.screen_rect.left:
            self.x -= self.settings.doodler_speed_factor

        if self.moving_up and self.doodler_rect.top > self.screen_rect.top:
            #self.ship_rect.centerx += 1
            self.y -= self.settings.doodler_speed_factor

        if self.moving_down and self.doodler_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.doodler_speed_factor
        # Update rect obj from self.center.
        #print(self.center)

        self.doodler_rect.centerx = self.x
        self.doodler_rect.centery = self.y


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.doodler_rect)
