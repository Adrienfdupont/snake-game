import pygame
from pygame import mixer
from snake_piece import Snake_piece
import os

class Snake:
    def __init__(self, window_width, window_height):

        mixer.init()
        self.width = 15
        self.color = (0, 255, 0)
        self.velocity = 15

        self.head = Snake_piece(window_width // 2, window_height // 2, self.width, self.color, None)
        self.head_move = None
        self.last_piece = self.head

        for i in range(1, 5):
            self.add_piece(self.head.rect.x - i * self.width, self.head.rect.y, self.last_piece)

    def add_piece(self, pos_x, pos_y, peer = None):
        piece = Snake_piece(pos_x, pos_y, self.width, self.color, peer)
        self.last_piece = piece

    def change_dir_left(self):
        if self.head_move != (self.velocity, 0) and self.head_move != None:
            self.head_move = (-self.velocity, 0)
        
    def change_dir_right(self):
        if self.head_move != (-self.velocity, 0):
            self.head_move = (self.velocity, 0)

    def change_dir_up(self):
        if self.head_move != (0, self.velocity):
            self.head_move = (0, -self.velocity)
    
    def change_dir_down(self):
        if self.head_move != (0, -self.velocity):
            self.head_move = (0, self.velocity)

    def update(self, window_width, window_height, fruits, game):
        # manage moving
        if self.head_move != None:
            self.head.previous_x = self.head.rect.x
            self.head.previous_y = self.head.rect.y
            self.head.rect.x += self.head_move[0]
            self.head.rect.y += self.head_move[1]
            Snake_piece.instances.update(self.head, game)

        # manage eating
        if pygame.sprite.groupcollide(Snake_piece.instances, fruits, False, False):
            fruits.update(window_width, window_height)
            self.add_piece(self.last_piece.previous_x, self.last_piece.previous_y, self.last_piece)
            sound = mixer.Sound(os.path.join("assets", "sounds", "eat.wav"))
            sound.play()

        # check overflow
        if self.head.rect.x < 0 or self.head.rect.x > window_width or self.head.rect.y < 0 or self.head.rect.y > window_height:
            game.clear()