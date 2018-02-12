class Settings():
    """A class to store all settings for Doodler Fight."""

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600
        self.doodler_speed_factor = 5
        self.bg_color = (230,230,230)
        # Bullet settings. Create a grey bullet with a width of 3 pixels and a height of 15 pixels.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 220
        self.bullets_allowed = 8
        self.bullet_radius = 5
