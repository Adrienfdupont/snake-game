import pygame
from snake_piece import Snake_piece

class Snake:

    def __init__(self, game_width, game_height):
        piece_width = 20
        piece_height = 20
        piece_color = (0, 255, 0)

        head_pos = (game_width // 2, game_height // 2)

        self.dir = "left"
        self.head_pos = []
        self.pieces = pygame.sprite.Group()
        for i in range(3):
            piece = Snake_piece(head_pos[0] - i * piece_width,
            head_pos[1],
            piece_width,
            piece_height,
            piece_color
        )
            self.pieces.add(piece)

    def move_left(self):
        if self.dir != "right":
            self.dir = "left"
            self.head_pos.append((self.x_pos, self.y))
        