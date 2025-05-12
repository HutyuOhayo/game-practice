import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from pygame.sprite import Group


def run_game():

    pygame.init

    pygame.display.set_caption('Allien Invasion')

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, aliens,
                         bullets)
if __name__ == '__main__':
    run_game()