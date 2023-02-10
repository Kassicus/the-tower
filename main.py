import pygame
import lib
import level

pygame.init()

class Game():
    def __init__(self):
        self.screen = lib.display_surface
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()

        self.level = level.Level()

    def run(self):
        while self.running:
            self.event_handler()
            self.draw()
            self.update()

    def event_handler(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(lib.color.BLACK)

        self.level.draw()

    def update(self):
        self.level.update()

        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()