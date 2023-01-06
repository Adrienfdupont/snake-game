import pygame
from fruit import Fruit

class Snake_piece(pygame.sprite.Sprite):

    instances = pygame.sprite.Group()

    def __init__(self, pos_x, pos_y, width, color, peer):    
        super().__init__()
        Snake_piece.instances.add(self)

        self.image = pygame.Surface([width, width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.previous_x = None
        self.previous_y = None
        self.peer = peer
        
    def update(self, head):
        if self == head:
            if pygame.sprite.groupcollide(Snake_piece.instances, Fruit.instances, False, True):
                Fruit(500, 500)
        else:
            self.previous_x = self.rect.x
            self.previous_y = self.rect.y
            self.rect.x = self.peer.previous_x
            self.rect.y = self.peer.previous_y
        