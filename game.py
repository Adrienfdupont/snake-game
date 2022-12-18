import pygame
from snake_piece import Snake_piece

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")

        # create game window
        width, height = 1280, 720
        self.window = pygame.display.set_mode((width, height))
        
        # generate player
        snake_head = Snake_piece(width, height)
        self.snake_pieces = pygame.sprite.Group()
        self.snakes.add(snake_head)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.handle_input()
            self.render()

    def render(self):
        self.window.fill((0,0,0))
        self.snakes.draw(self.window)
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            