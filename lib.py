import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "The Tower"

class ColorLibrary():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

color = ColorLibrary()
display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
delta_time = 0
fps_limit = 30