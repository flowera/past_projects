import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def fire_bullet(settings, screen, ship, bullets):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # ReDraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    # ReDraw all bullets behind ship and aliens.

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #print(bullets)

    # Call function draw ship in current location.
    ship.blitme()
    # Make the most recent drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    #bullets.update()
    for i in bullets:
        i.update_bullet()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.bullet_rect.right >= 1000:
            bullets.remove(bullet)
    #print(len(bullets))
