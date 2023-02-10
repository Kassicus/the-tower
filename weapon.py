import pygame
import lib

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([300, 85])
        self.image.fill(lib.color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update(self):
        pass