import pygame
from snake_piece import Snake_piece

class Snake:

    def __init__(self, game_width, game_height):
        piece_width = 20
        piece_height = 20
        color = (0, 255, 0)

        x_start = game_width // 2
        y_start = game_height // 2

        self.head = [x_start, y_start]
        self.dir = None
        self.body = pygame.sprite.Group()
        for i in range(3):
            piece = Snake_piece(
                x_start - i * piece_width,
                y_start,
                piece_width,
                piece_height,
                color
            )
            self.body.add(piece)

    def change_dir(self, key):
        if key == pygame.K_LEFT and self.dir != "right":
            self.dir = "left"
        elif key == pygame.K_RIGHT and self.dir != "left":
            self.dir = "right"
        elif key == pygame.K_UP and self.dir != "down":
            self.dir = "up"
        elif key == pygame.K_DOWN and self.dir != "up":
            self.dir = "down"

    def update(self):
        if self.dir == None:
            return
        match self.dir:
            case "left":
                self.head[0] -= 1
            case "right":
                self.head[0] += 1
            case "up":
                self.head[1] -= 1
            case "down":
                self.head[1] += 1