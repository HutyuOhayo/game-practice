import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from pygame.sprite import Group
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button

def run_game():

    pygame.init()

    pygame.display.set_caption('Allien Invasion')

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Button(ai_settings, screen, "Play")
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
bullets, play_button)


if __name__ == '__main__':
    run_game()