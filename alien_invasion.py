import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()

    ai_setting = Settings()

    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))

    ship = Ship(ai_setting, screen)

    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    gf.create_fleet(ai_setting, screen, aliens)

    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)

run_game()
