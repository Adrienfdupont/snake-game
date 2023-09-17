import pygame
import os
from snake import Snake
from fruit import Fruit
from snake_piece import Snake_piece

class Game:
    def __init__(self):
        # game init
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.window_width = 720
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.score_font = pygame.font.Font(os.path.join("assets", "fonts", "RollboxBoldItalic-ZVx0q.ttf"), 18)
        self.score = 0

        # entities init
        self.snake = Snake(self.window_width, self.window_height)
        Fruit(self.window_width, self.window_height)

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
        previous_size = len(Snake_piece.instances)
        self.snake.update(self.window_width, self.window_height, Fruit.instances)
        if len(Snake_piece.instances) > previous_size:
            self.score += 1

    def render(self):
        self.window.fill((0,0,0))
        score_surface = self.score_font.render(f'Score  {str(self.score)}', True, (255, 255, 255))
        self.window.blit(score_surface, (self.window_width // 2 - 50, 20))

        Snake_piece.instances.draw(self.window)
        Fruit.instances.draw(self.window)
        pygame.display.flip()

            