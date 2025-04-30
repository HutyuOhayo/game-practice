import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():

    pygame.init

    screen_width, screen_height = 1200, 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('Allien Invasion')

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    bullets = Group()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

if __name__ == '__main__':
    run_game()