import pygame
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "The Tower"

class ColorLibrary():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.RED = pygame.Color(255, 0, 0, 255)
        self.GREEN = pygame.Color(0, 255, 0, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)
        self.YELLOW = pygame.Color(255, 255, 0, 255)
        self.MAGENTA = pygame.Color(255, 0, 255, 255)
        self.CYAN = pygame.Color(0, 255, 255, 255)

    def random_color(self):
        col = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        return(col)

color = ColorLibrary()
display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
delta_time = 0
fps_limit = 30
events = pygame.event.get()