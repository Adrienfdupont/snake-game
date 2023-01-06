from snake_piece import Snake_piece

class Snake:

    def __init__(self, window_width, window_height):

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
        if self.head_move != (self.velocity, 0):
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

    def update(self):
        if self.head_move != None:
            self.head.previous_x = self.head.rect.x
            self.head.previous_y = self.head.rect.y
            self.head.rect.x += self.head_move[0]
            self.head.rect.y += self.head_move[1]
            Snake_piece.instances.update(self.head)