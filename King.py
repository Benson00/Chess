
from typing import override
import Piece


class King(Piece):
    
    def __init__(self, color):
        super().__init__(color)
    
def get_allowed_moves(self, r, c):
    allowed_moves = []

    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in moves:
        new_row = r + dr
        new_col = c + dc
        
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:
            allowed_moves.append((new_row, new_col))

    return allowed_moves