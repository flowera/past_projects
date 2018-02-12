import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.bullet_rect = pygame.Rect(0, 0, settings.bullet_width,settings.bullet_height)

        self.bullet_rect.centery = ship.doodler_rect.centery
        self.bullet_rect.left = ship.doodler_rect.right
        self.pos = (self.bullet_rect.centerx, self.bullet_rect.centery)
        self.radius = settings.bullet_radius
        # Store the bullet's position as a decimal value.
        self.x = float(self.bullet_rect.right)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
    def update_bullet(self):
        """Move the bullet right the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.bullet_rect.x = self.x
        self.pos = (self.bullet_rect.centerx, self.bullet_rect.centery)
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        #pygame.draw.rect(self.screen, self.color, self.bullet_rect)
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
