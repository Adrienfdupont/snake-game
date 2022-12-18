import pygame
import random

class Snake_piece(pygame.sprite.Sprite):

    def __init__(self, game_width, game_height):
        super().__init__()

        width, height = 10, 10
        color = (0, 255, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, game_width - width)
        self.rect.y = random.randint(0, game_height - height)