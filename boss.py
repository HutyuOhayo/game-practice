import pygame
from alien import Alien

class Boss(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/boss.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.maxhp = 50
        self.hpcount = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.boss_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def hit(self):
        self.hpcount += 1
        return self.hpcount >= self.maxhp