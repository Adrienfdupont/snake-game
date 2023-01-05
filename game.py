import pygame
from snake import Snake
from fruit import Fruit
from snake_piece import Snake_piece

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        width, height = 1280, 720

        self.window = pygame.display.set_mode((width, height))
        self.snake = Snake(width, height)

        self.fruit = Fruit(width, height)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_input(event.key)
            self.update()
            self.render()

    def handle_input(self, key):
        if key == pygame.K_LEFT:
            self.snake.change_dir_left()
        elif key == pygame.K_RIGHT:
            self.snake.change_dir_right()
        elif key == pygame.K_UP:
            self.snake.change_dir_up()
        elif key == pygame.K_DOWN:
            self.snake.change_dir_down()

    def update(self):
        self.snake.update(self.fruit)

    def render(self):
        self.window.fill((0,0,0))
        Snake_piece.instances.draw(self.window)
        Fruit.instances.draw(self.window)
        pygame.display.flip()
            

            