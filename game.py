import pygame
from snake import Snake
from snake_piece import Snake_piece

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
            self.handle_input()
            self.render()
            self.update()

    def render(self):
        self.window.fill((0,0,0))
        self.snake.draw(self.window)
        pygame.display.flip()

    def update(self):
        self.snake.pieces.draw(self.window)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        self.snake.move_left()
                    case pygame.K_RIGHT:
                        self.snake.move_right()
                    case pygame.K_UP:
                        self.snake.move_up()           
                    case pygame.K_DOWN:
                        self.snake.move_down()
            

            