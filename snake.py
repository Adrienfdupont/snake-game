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

    def update(self):
        if self.dir == None:
            return
        self.head[0] += self.dir[0]
        self.head[1] += self.dir[1]