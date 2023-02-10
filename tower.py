import pygame
import lib

class Zone(pygame.sprite.Sprite):
    def __init__(self, x, y, parent):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        
        self.parent = parent

        self.image = pygame.Surface([300, 85])
        self.image.fill(lib.color.CYAN)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in lib.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.x < mouse_x < self.rect.x + self.rect.width:
                    if self.rect.y < mouse_y < self.rect.y + self.rect.height:
                        t = Tower(self.pos.x, self.pos.y)
                        self.parent.towers.add(t)
                        self.parent.current_tower_level += 1
                        self.parent.create_zone()
                        self.kill()

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([300, 85])
        self.image.fill(lib.color.random_color())
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update(self):
        pass