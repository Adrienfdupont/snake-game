import pygame
from snake import Snake

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        width, height = 1280, 720

        self.window = pygame.display.set_mode((width, height))
        self.snake = Snake(width, height)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_input(event.key)
            self.update()
            self.render()

    def handle_input(self, key):
        if (key == pygame.K_LEFT or key == pygame.K_UP
        or key == pygame.K_RIGHT or key == pygame.K_DOWN):
            self.snake.change_dir(key)

    def update(self):
        self.snake.update()
        self.snake.body.update(self.snake.head)

    def render(self):
        self.window.fill((0,0,0))
        self.snake.body.draw(self.window)
        pygame.display.flip()
            

            