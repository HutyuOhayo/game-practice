class Settings():

    def __init__(self):
        self.ship_speed_factor = 3
        self.ship_limit = 3

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 230, 230, 230, 0

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.bullet_speed_factor = 3

        self.boss_speed_factor = 2
        self.boss_hp = 50
        self.boss_points = 1000

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
        self.boss_points = 1000

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.boss_points = 1000
        print(self.alien_points, self.boss_points)