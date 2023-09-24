import pygame
import os
from snake import Snake
from fruit import Fruit
from snake_piece import Snake_piece

class Game:
    def __init__(self):
        pygame.init()

        # set window
        pygame.display.set_caption("Snake Game")
        self.window_width = 720
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # set fonts
        game_over_font = pygame.font.Font(os.path.join("assets", "fonts", "RollboxBoldItalic-ZVx0q.ttf"), 36)
        self.game_over_surface = game_over_font.render("Game over", True, (0, 255, 0))

        message_font = pygame.font.Font(os.path.join("assets", "fonts", "RollboxBoldItalic-ZVx0q.ttf"), 18)
        self.message_surface = message_font.render("Press the space bar to play", True, (0, 255, 0))

        self.score_font = pygame.font.Font(os.path.join("assets", "fonts", "RollboxBoldItalic-ZVx0q.ttf"), 18)

        # launch game
        self.game_over = False
        self.create()

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
        elif key == pygame.K_SPACE:
            if self.game_over == True:
                self.create()
                self.game_over = False

    def update(self):
        previous_size = len(Snake_piece.instances)
        self.snake.update(self.window_width, self.window_height, Fruit.instances, self)
        if len(Snake_piece.instances) > previous_size:
            self.score += 1

    def render(self):
        self.window.fill((0, 0, 0))

        # refresh score surface
        self.score_surface = self.score_font.render(f'Score  {str(self.score)}', True, (255, 255, 255))
        self.window.blit(self.score_surface, (self.window_width // 2 - self.score_surface.get_width() // 2, 20))

        # print game over screen
        if self.game_over == True:
            self.window.blit(self.game_over_surface, (self.window_height // 2 - self.game_over_surface.get_width() // 2, self.window_height // 2 - self.game_over_surface.get_height()))
            self.window.blit(self.message_surface, (self.window_height // 2 - self.message_surface.get_width() // 2, self.window_height // 2  + self.message_surface.get_height()))

        Snake_piece.instances.draw(self.window)
        Fruit.instances.draw(self.window)
        pygame.display.flip()

    def clear(self):
        self.game_over = True
        for piece in Snake_piece.instances:
            piece.kill()
        for fruit in Fruit.instances:
            fruit.kill()

    def create(self):
        self.score = 0
        self.snake = Snake(self.window_width, self.window_height)
        Fruit(self.window_width, self.window_height)