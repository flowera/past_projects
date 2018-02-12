import pygame
from settings import Settings

class Rocket():
    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.png')
        self.rocket_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new rocket at the bottom left of the screen.
        self.rocket_rect.left = self.screen_rect.left
        self.rocket_rect.bottom = self.screen_rect.bottom

        # Store a decimal value for rocket's center
        self.x = float(self.rocket_rect.centerx)
        self.y = float(self.rocket_rect.centery)
        """print('self.centerx %d' % (self.x))
        print('self.centery %d' % (self.y))
        print('self.x %d' % (self.rocket_rect.x))
        print('self.y %d' % (self.rocket_rect.y))
        print(self.rocket_rect)"""
        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            #self.ship_rect.centerx += 1
            self.x += self.settings.rocket_speed_factor

        if self.moving_left and self.rocket_rect.left > self.screen_rect.left:
            self.x -= self.settings.rocket_speed_factor

        if self.moving_up and self.rocket_rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed_factor

        if self.moving_down and self.rocket_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed_factor

        # Update rect obj from self.center.
        self.rocket_rect.centerx = self.x
        self.rocket_rect.centery = self.y

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rocket_rect)
