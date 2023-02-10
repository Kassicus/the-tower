import pygame
import lib
import tower

class Level():
    def __init__(self):
        self.current_tower_level = 0

        self.towers = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()

        self.create_zone()

    def create_zone(self):
        if self.current_tower_level < 9:
            z = tower.Zone(500, int(750 - (self.current_tower_level * 85)), self)
            self.zones.add(z)

    def draw(self):
        self.towers.draw(lib.display_surface)
        self.zones.draw(lib.display_surface)

    def update(self):
        self.zones.update()

