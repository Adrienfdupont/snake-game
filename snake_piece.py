import pygame

class Snake_piece(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, width, height, color):    
        super().__init__()       
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.route = []

    def update(self, head):
        self.route.append(head)
        self.rect.x = self.route[0][0]
        self.rect.y = self.route[0][1]
        del self.route[0]