import pygame
import random
import os

class Fruit(pygame.sprite.Sprite):
    instances = pygame.sprite.Group()

    def __init__(self, window_width, window_height):
        super().__init__()

        Fruit.instances.add(self)
        self.width = 20
        self.window_width = window_width
        self.window_height = window_height
        colors = ("green.png", "red.png", "purple.png", "yellow.png")
        
        image = os.path.join("assets", "images", random.choice(colors))
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (self.width, self.width))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.width)
        self.rect.y = random.randint(0, window_height - self.width)

    def update(self, window_width, window_height, snake, snake_pieces):
        if pygame.sprite.groupcollide(snake_pieces, Fruit.instances, False, True):
            snake.eat()
            self.reset(window_width, window_height)

    def reset(self, window_width, window_height):
        Fruit.instances.remove(self)
        Fruit(window_width, window_height)