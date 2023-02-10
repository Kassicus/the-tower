import pygame
import lib

pygame.init()

class Game():
    def __init__(self):
        self.screen = lib.display_surface
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

    def run(self):
        while self.running:
            self.event_handler()
            self.draw()
            self.update()

    def event_handler(self):
        self.events = pygame.event.get()

        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(lib.color.WHITE)

    def update(self):
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()