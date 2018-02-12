class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600
        self.ship_speed_factor = 5
        self.bg_color = (230,230,230)
        # Bullet settings. Create a grey bullet with a width of 3 pixels and a height of 15 pixels.
        self.bullet_speed_factor = 13
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
