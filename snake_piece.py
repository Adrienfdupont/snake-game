import pygame

class Snake_piece(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, width, height, color):    
        super().__init__()       
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self, pos):
        